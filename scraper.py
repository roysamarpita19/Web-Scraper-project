# scraper.py

import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
    
    def get_soup(self):
        """Helper function to get BeautifulSoup object from a URL"""
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    
    def scrape_titles(self):
        """Scrapes titles from a blog or news website"""
        soup = self.get_soup()
        # Example for scraping article titles
        titles = []
        for article in soup.find_all('h2'):  # Change the tag depending on the website's structure
            title = article.get_text()
            titles.append(title)
        return titles
