import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

def main():
    url = 'https://example.com'
    title = scrape_website(url)
    print(f'The title of the website is: {title}')

if __name__ == '__main__':
    main()
