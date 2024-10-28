import * as fs from 'node:fs';
import * as path from 'node:path';
import * as vscode from 'vscode';
import { CompletionItem, CompletionItemKind, type Disposable, Hover, languages } from 'vscode';

interface CloudFormationTemplate {
  Resources?: { [key: string]: any };
}

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
  public getResourceSnippet(resourceType: string): string {
    const resourceData = this.resourceMap.get(resourceType);
    if (!resourceData) return '';

    let snippet = `LogicalID:\n  Type: ${resourceType}\n  Properties:\n`;
    snippet += this.generatePropertiesSnippet(resourceData.Properties, 4);
    return snippet;
  }

  private generatePropertiesSnippet(properties: any, indent: number): string {
    let snippet = '';
    for (const [key, value] of Object.entries(properties)) {
      const indentation = ' '.repeat(indent);
      if (typeof value === 'object') {
        snippet += `${indentation}${key}:\n`;
        snippet += this.generatePropertiesSnippet(value, indent + 2);
      } else {
        snippet += `${indentation}${key}: "${value}"\n`;
      }
    }
    return snippet;
  }

  private loadResourceMap() {
    const filePath = path.join(__dirname, '..', 'snippets', 'raw-cfn-resources-output.json');
    outputChannel.appendLine(`Loading resource map from: ${filePath}`);

    try {
      const rawData = fs.readFileSync(filePath, 'utf8');
      const resources: { [key: string]: ResourceData } = JSON.parse(rawData);

      for (const [resourceName, resourceData] of Object.entries(resources)) {
        this.resourceMap.set(resourceName, resourceData);
      }
      outputChannel.appendLine(`Loaded ${this.resourceMap.size} resources`);
      outputChannel.appendLine(`Resource names: ${Array.from(this.resourceMap.keys()).join(', ')}`);
    } catch (error) {
      outputChannel.appendLine(`Error loading resource map: ${error}`);
    }
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

  public findNearestResourceType(document: vscode.TextDocument, position: vscode.Position): string | null {
    for (let i = position.line; i >= 0; i--) {
      const lineText = document.lineAt(i).text;
      const resourceType = this.extractResourceType(lineText);
      if (resourceType) {
        return resourceType;
      }
    }
    return null;
  }

  public getResourceTypeCompletions(): CompletionItem[] {
    const completions = Array.from(this.resourceMap.keys()).map((resourceType) => {
      const item = new CompletionItem(resourceType, CompletionItemKind.Class);
      item.detail = 'CloudFormation Resource Type';
      item.documentation = new vscode.MarkdownString(`[Documentation](${this.resourceMap.get(resourceType)?.Docs})`);
      item.insertText = new vscode.SnippetString(this.getResourceSnippet(resourceType));
      return item;
    });
    outputChannel.appendLine(`Providing ${completions.length} resource type completions`);
    return completions;
  }

  public getResourcePropertyCompletions(resourceType: string): CompletionItem[] {
    const resourceData = this.resourceMap.get(resourceType);
    if (!resourceData) {
      outputChannel.appendLine(`No resource data found for ${resourceType}`);
      return [];
    }

    const completions = Object.entries(resourceData.Properties).map(([propertyName, propertyType]) => {
      const item = new CompletionItem(propertyName, CompletionItemKind.Property);
      item.detail = `${propertyType}`;
      item.documentation = new vscode.MarkdownString(`Property of ${resourceType}`);
      return item;
    });
    outputChannel.appendLine(`Providing ${completions.length} property completions for ${resourceType}`);
    return completions;
  }
}

function isUnderResourcesKey(document: vscode.TextDocument, position: vscode.Position): boolean {
  const text = document.getText();
  const lines = text.split('\n');
  let inResources = false;
  let resourcesIndentation = -1;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.trim().startsWith('Resources:')) {
      inResources = true;
      resourcesIndentation = line.indexOf('Resources:');
    } else if (inResources && line.trim() !== '' && line.indexOf(line.trim()) <= resourcesIndentation) {
      inResources = false;
    }

    if (i === position.line) {
      return inResources;
    }
  }

  return false;
}

export function activate(context: vscode.ExtensionContext) {
  outputChannel = vscode.window.createOutputChannel('CloudFormation Snippets');
  outputChannel.show(); // Uncomment this line to show the output channel
  outputChannel.appendLine('CloudFormation Snippets extension activated');

  const linkmappings = new LinkMappings();
  const disposable: Disposable[] = [];

  disposable.push(
    languages.registerCompletionItemProvider(['yaml', 'yml', 'json'], {
      provideCompletionItems(document, position, token, context) {
        outputChannel.appendLine(`Autocomplete triggered at position: ${position.line}:${position.character}`);

        const lineText = document.lineAt(position.line).text;
        const linePrefix = lineText.substr(0, position.character);
        outputChannel.appendLine(`Line prefix: ${linePrefix}`);

        // Always provide resource type completions
        const resourceTypeCompletions = linkmappings.getResourceTypeCompletions();
        outputChannel.appendLine(`Providing ${resourceTypeCompletions.length} resource type completions`);

        const resourceType = linkmappings.findNearestResourceType(document, position);
        if (resourceType) {
          const propertyCompletions = linkmappings.getResourcePropertyCompletions(resourceType);
          outputChannel.appendLine(`Providing ${propertyCompletions.length} property completions for ${resourceType}`);
          return [...resourceTypeCompletions, ...propertyCompletions];
        }

        return resourceTypeCompletions;
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
