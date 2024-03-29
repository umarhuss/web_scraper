# request libaraies needed 
import requests
from bs4 import BeautifulSoup

#headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

property_url = 'https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=3&maxBedrooms=3&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare='

response = requests.get(property_url, headers=headers)
print(response.status_code)
page_content = response.text

# use beautifulsoup to parse our information 


# create csv file 



'''choose website:
i have chosen rightmove to scrape 

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