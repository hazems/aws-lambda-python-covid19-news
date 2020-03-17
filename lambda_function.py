# Simple AWS Lambda Python Function to get the latest news about Corona Virus.
import requests
import json

# Put your API key here, get it from https://newsapi.org/
NEWS_API_KEY = '<<API_KEY>>'

class Headline:
    def __init__(self, author, title, description, articleTime):
      self._author = author
      self._title = title
      self._description = description
      self._articleTime = articleTime
    def __str__(self):
      return "author=%s, title=%s, description=%s, articleTime=%s" % (self._author, self._title, self._description, self._articleTime)
            
def retrieveCoronaHeadlines():
  URL = "http://newsapi.org/v2/top-headlines?country=us&q=corona&sortBy=publishedAt&apiKey=" + NEWS_API_KEY    
  response = requests.get(url = URL) 
  data = response.json()
  output = []
  
  if data['status'] != 'ok':
    return {
      'statusCode': 500,
      'body': json.dumps('An Error occurs')
    }

  for article in data['articles']:
    output.append(Headline(article['author'], article['title'], article['content'], article['publishedAt']))
    
  return {
    'statusCode': 200,
    'body': json.dumps(output, default=lambda x: x.__dict__)
  }

def lambda_handler(event, context):
  return retrieveCoronaHeadlines()
