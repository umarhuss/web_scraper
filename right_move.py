import requests 
from bs4 import BeautifulSoup as bs

#class to encapsulate functionality of the scrapper 
class rightmove_scraper:
    def fetch(self,url):
        print(f'The GET request to the url: {url}', end='')
        try:
            response = requests.get(url)
            response.raise_for_status() #raises httpError if an error code is returned
            print(f'Status Code: {response.status_code}') #prints the status code to the console
            return response
        except requests.RequestException as err:
            print(f'Error ocurred:{err}')
            return response
