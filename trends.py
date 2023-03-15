from pytrends import TrendReq

# Create a Google Trends API client
pytrends = TrendReq()

# Get the top 10 trending searches in the United States for the past hour
trending_searches = pytrends.trending_searches(pn='united_states')
print(trending_searches)