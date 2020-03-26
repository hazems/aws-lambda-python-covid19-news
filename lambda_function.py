# Simple AWS Lambda Python Function to get the latest news about Corona Virus.
import requests
import json

NEWS_API_KEY = '<<YOUR_API_KEY>>'

class Headline:
    def __init__(self, author, title, description, articleTime, newsUrl, imageUrl):
      self.author = author
      self.title = title
      self.description = description
      self.articleTime = articleTime
      self.newsUrl = newsUrl
      self.imageUrl = imageUrl
    def __str__(self):
      return "author=%s, title=%s, desc=%s, time=%s, newsUrl=%s, imageUrl=%s" % (self.author, self.title, 
      self.description, self.articleTime, self.newsUrl, self.imageUrl)
            
def retrieveCoronaHeadlines():
  URL = "http://newsapi.org/v2/top-headlines?country=us&q=corona&sortBy=publishedAt&apiKey=" + NEWS_API_KEY    
  response = requests.get(url = URL) 
  data = response.json()
  output = []
  
  if data['status'] != 'ok':
    return {
      'statusCode': 500,
      'headers': {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "GET"
      },
      'body': json.dumps('An Error occurs')
    }

  for article in data['articles']:
    output.append(Headline(article['author'], article['title'], article['content'], 
    article['publishedAt'], article['url'], article['urlToImage']))
    
  return {
    'statusCode': 200,
    'headers': {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "*",
      "Access-Control-Allow-Methods": "GET"
    },
    'body': json.dumps(output, default=lambda x: x.__dict__)
  }

def lambda_handler(event, context):
  return retrieveCoronaHeadlines()