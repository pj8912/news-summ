import requests
from bs4 import BeautifulSoup

url = 'https://www.thetimes.co.uk/article/putin-russian-economy-stock-market-price-ukraine-war-2023-70zs8dss8'

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the URL using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first 'meta' tag with property 'og:image'
og_image = soup.find('meta', property='og:image')

# Extract the 'content' attribute of the 'meta' tag
img_url = og_image['content']

print(img_url)