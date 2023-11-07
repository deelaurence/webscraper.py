import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    print("here in scrape function")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text content within the HTML structure
        all_text = ' '.join([element.get_text() for element in soup.find_all(text=True)])

        return all_text
    else:
        return None

# print(scrape_website("https://jumia.com.ng"))