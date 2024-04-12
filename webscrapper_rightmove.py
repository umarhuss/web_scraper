# Request libraies needed. 
import requests
from bs4 import BeautifulSoup

# Headers to mimic a browser request.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

property_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=3&maxBedrooms=3&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare=#prop145942733'

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

for link in property_info:
    href = link.get("href")
    if href:
        full_link = "https://www.rightmove.co.uk" + href
        all_links.append(full_link)



    
# Create csv file. 



'''choose website:
i have chosen rightmove to scrap

we will get a list of properties. for each property we will  grab:
- The property page url 

for each property we will grab:

- The name and location of the property 
- The type 
- number of bedrooms 
- number of bathrooms 
- price  
'''