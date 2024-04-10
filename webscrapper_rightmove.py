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
address_tag =[]
location_divs = document.find_all('address', class_='propertyCard-address')
for element in location_divs:
    address_tag.append(element.find_all('span'))

if address_tag:
    for address in address_tag:
        for span_element in address:
            property_location = span_element.text.strip()
            print(f'Location: {property_location}')
    else:
        print("Location not found")


# Get all prices for each property on page 
price_divs = document.find_all('span',{'class':'propertyCard-priceValue'})

if price_divs:
    for price_div in price_divs:
        price = price_div.text.strip()
        print("Price:", price)
else:
    print("Price not found.")


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
- furnished or unfurnished 
- size  
'''