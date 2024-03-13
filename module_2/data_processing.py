#Input:
#Code expects the input of a URL to be completed

#Output:
#If successful, output will be the scraped article
#If unsuccessful, output will be "Just go ahead and change your major =P"

#Working:
#Scrapes the article content from the provided URL using requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    """Scrape article content from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        article_content = soup.find('div', class_='showBlogPage')
        if article_content:
            return article_content.get_text(separator='\n')
        else:
            return "Just go ahead and change your major =P"
    except requests.exceptions.RequestException as e:
        print("Error fetching URL.")
        return None

