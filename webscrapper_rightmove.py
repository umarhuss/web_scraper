# Request libraies needed. 
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Headers to mimic a browser request.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

property_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare='
response = requests.get(property_url, headers=headers)
print(response.status_code)
page_content = response.text

# Use beautifulsoup to parse our information. 
document = BeautifulSoup(page_content,'html.parser')

# Get the address for all propertys on page 
all_addresses = []
location_divs = document.find_all('address', class_='propertyCard-address')

for element in location_divs:
    spans = element.find_all('span')
    for span_element in spans:
        all_addresses.append(span_element.text.strip())

# # Get all prices for each property on page 
all_prices = []
for price in document.find_all('span',class_='propertyCard-priceValue'):
    all_prices.append(price.text.strip())


#Get number of beds/description
all_descriptions = []
for description in document.find_all("h2", class_="propertyCard-title"):
    all_descriptions.append(description.text.strip())

# Get links for each property
all_links = []
property_info = document.find_all('a', class_='propertyCard-link')
# Expecting 25 links as 25 peroperties are on the page 
num_properties = min(len(location_divs), 25)  
for i in range(num_properties):
    link = property_info[i].get("href")
    if link:
        full_link = "https://www.rightmove.co.uk" + link
        all_links.append(full_link)

max_length = max(len(all_addresses), len(all_prices), len(all_descriptions), len(all_links))
all_addresses += [[]] * (max_length - len(all_addresses))
all_prices += [''] * (max_length - len(all_prices))
all_descriptions += [''] * (max_length - len(all_descriptions))
all_links += [''] * (max_length - len(all_links))

for i in range(max_length):
    if not all_addresses[i]:
        all_addresses[i] = ['No address found']
    if not all_prices[i]:
        all_prices[i] = 'No price found'
    if not all_descriptions[i]:
        all_descriptions[i] = 'No description found'
    if not all_links[i]:
        all_links[i] = 'No link found'


    
# Create csv file. 
data ={
    'Address': all_addresses,
    'Description': all_descriptions,
    'Price': all_prices,
    'Links': all_links
}

data_frame = pd.DataFrame.from_dict(data)
data_frame.to_csv(r"property_data.csv", encoding="utf-8", header="true", index = False)


