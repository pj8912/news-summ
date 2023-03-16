from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
load_dotenv()


NEWSAPI_KEY=os.environ.get("NEWSAPI_KEY")


def getnews():
    newsapi = NewsApiClient(api_key=NEWSAPI_KEY)
    top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
    
    all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    sources = newsapi.get_sources()
    return all_articles
