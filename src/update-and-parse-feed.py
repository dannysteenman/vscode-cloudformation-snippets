import feedparser

NewsFeed = feedparser.parse(
    "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-cloudformation-release-notes.rss"
)
entry = NewsFeed.entries[0]

print(entry.summary)
