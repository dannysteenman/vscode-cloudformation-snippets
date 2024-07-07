import * as fs from 'node:fs';
import * as path from 'node:path';
import * as vscode from 'vscode';
import { type Disposable, Hover, languages } from 'vscode';

let outputChannel: vscode.OutputChannel;

interface ResourceData {
  Docs: string;
  Properties: { [key: string]: string };
}

class LinkMappings {
  private resourceMap: Map<string, ResourceData> = new Map();

  constructor() {
    this.loadResourceMap();
  }

  private loadResourceMap() {
    const filePath = path.join(__dirname, '..', 'snippets', 'raw-cfn-resources-output.json');
    const rawData = fs.readFileSync(filePath, 'utf8');
    const resources: { [key: string]: ResourceData } = JSON.parse(rawData);

    for (const [resourceName, resourceData] of Object.entries(resources)) {
      this.resourceMap.set(resourceName, resourceData);
    }
    outputChannel.appendLine(`Loaded ${this.resourceMap.size} resources`);
  }

  public getLink(document: vscode.TextDocument, position: vscode.Position): string | null {
    const lineText = document.lineAt(position.line).text;
    outputChannel.appendLine(`Processing line: ${lineText}`);

    const resourceType = this.extractResourceType(lineText);
    if (resourceType) {
      const resourceData = this.resourceMap.get(resourceType);
      if (resourceData) {
        outputChannel.appendLine(`Found resource type: ${resourceType}`);
        return `Find documentation for this resource at: ${resourceData.Docs}`;
      }
    }

    const propertyName = this.extractPropertyName(lineText);
    if (propertyName) {
      outputChannel.appendLine(`Found property: ${propertyName}`);
      const resourceType = this.findNearestResourceType(document, position);
      if (resourceType) {
        outputChannel.appendLine(`Found nearest resource type: ${resourceType}`);
        const resourceData = this.resourceMap.get(resourceType);
        if (resourceData && propertyName in resourceData.Properties) {
          const propertyType = resourceData.Properties[propertyName];
          let url: string;
          // Check if the property type is not a primitive type
          if (!['String', 'Number', 'Boolean'].includes(propertyType)) {
            // Use the "aws-properties-" URL structure with the property type
            const baseUrl = 'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-';
            const urlSuffix = `${resourceType.split('::')[1].toLowerCase()}-${resourceType.split('::')[2].toLowerCase()}-${propertyType.toLowerCase()}.html`;
            url = baseUrl + urlSuffix;
          } else {
            // For primitive types, use the "#cfn-" URL structure with the property name
            url = `${resourceData.Docs}#cfn-${resourceType.split('::')[1].toLowerCase()}-${resourceType.split('::')[2].toLowerCase()}-${propertyName.toLowerCase()}`;
          }
          return `Find documentation for this property at: ${url}`;
        }
      }
    }

    outputChannel.appendLine('No link found');
    return null;
  }

  private extractResourceType(text: string): string | null {
    const regex = /(?:Type:\s*)(['"]?)(AWS::[^'"]+)\1/;
    const match = text.match(regex);
    return match ? match[2] : null;
  }

  private extractPropertyName(text: string): string | null {
    const regex = /^\s*(\w+):/;
    const match = text.match(regex);
    return match ? match[1] : null;
  }

  private findNearestResourceType(document: vscode.TextDocument, position: vscode.Position): string | null {
    for (let i = position.line; i >= 0; i--) {
      const lineText = document.lineAt(i).text;
      const resourceType = this.extractResourceType(lineText);
      if (resourceType) {
        return resourceType;
      }
    }
    return null;
  }
}

export function activate(context: vscode.ExtensionContext) {
  outputChannel = vscode.window.createOutputChannel('CloudFormation Snippets');
  outputChannel.show();
  outputChannel.appendLine('CloudFormation Snippets extension activated');

  const linkmappings = new LinkMappings();
  const disposable: Disposable[] = [];

  disposable.push(
    languages.registerHoverProvider(['yaml', 'yml', 'json'], {
      provideHover(document, position, token) {
        outputChannel.appendLine(`Hover triggered at position: ${position.line}:${position.character}`);
        return getLink(document, position, linkmappings);
      },
    }),
  );

  // biome-ignore lint/complexity/noForEach: <explanation>
  disposable.forEach((provider) => {
    context.subscriptions.push(provider);
  });
}

export function deactivate() {
  outputChannel.appendLine('CloudFormation Snippets extension deactivated');
}

function getLink(document: vscode.TextDocument, position: vscode.Position, linkmappings: LinkMappings): Hover | null {
  const link = linkmappings.getLink(document, position);

  if (!link) {
    outputChannel.appendLine('No link returned');
    return null;
  }

  outputChannel.appendLine(`Returning hover with link: ${link}`);
  return new Hover(new vscode.MarkdownString(link, true));
}
