from pytrends.request import TrendReq
import pandas as pd


# Create a Google Trends API client
pytrends = TrendReq()



# Get the top 10 trending searches in the United States for the past hour
trending_searches = pytrends.trending_searches(pn='india')
# print(trending_searches.head())
# print(type(trending_searches))

print(trending_searches)
