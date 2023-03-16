from pytrends.request import TrendReq

# Create a Google Trends API client
pytrends = TrendReq()

# Get the top 50 trending searches in the United States for the past hour
trending_searches = pytrends.trending_searches(pn='united_states')

# Retrieve related topics for each search term
related_topics = []
for term in trending_searches:
    payload = {'keyword': term}
    related_topic = pytrends.related_topics(payload)
   
# Print the top 50 trending searches and their related topics
for i in range(len(trending_searches)):
    print(f'{i + 1}. {trending_searches[i]}')
    for j in range(len(related_topics[i]['rising']['topic_title'])):
        print(f'\t{j + 1}. {related_topics[i]["rising"]["topic_title"].iloc[j]}')
