# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import os
import pymongo
import pandas as pd
import time

def scrape():

    browser = init_browser()
    listings = {}
    
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(3)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(browser.html, 'html.parser')

    # Examine the results, then determine element that contains sought info
    # print(browser.html)

    # Retrieve all elements
    # articles = soup.find_all('div', class_='content_title')
    article = soup.find('li', class_='slide')
    # article_section = soup.find_all('li')
    # article_section.contents.find_all('li')
    # print(article)

    article_title_tag = article.find('div', class_='content_title')
    article_contents = article.find('div', class_='article_teaser_body')
    news_title = article_title_tag.text
    news_p = article_contents.text
    print(news_title)
    print(news_p)

    listings["news_title"] = news_title
    listings["news_p"] = news_p

    home_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(home_url)
    # print(browser.html)

    time.sleep(5)

    browser.click_link_by_partial_text('FULL IMAGE')

    time.sleep(5)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    # print(html)
    img_tag = soup.find('img', class_='fancybox-image')
    print(img_tag['src'])

    featured_image_url = 'https://www.jpl.nasa.gov' + img_tag['src']
    print(featured_image_url)

    listings["featured_image_url"] = featured_image_url

    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    tables

    type(tables)

    df = tables[0]
    df.head()

    html_table = df.to_html()
    html_table

    # Save to file
    df.to_html('table.html')

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # print(browser.html)

    time.sleep(5)

    html = browser.html
    soup = bs(html, 'html.parser')
    # print(html)
    img_items = soup.find_all('div', class_='item')
    # print(img_items)

    hemisphere_image_urls = []

    for img_item in img_items:
        # print('page:', img_item)
        # print('-------------------------------------------------------------------------------------------------------')
        title = img_item.find('h3')
        img_tag = img_item.find('img')
        link = img_tag['src']
        # print(title)
    #    print("Title: " + title.text)
    #    print("Link: " + link)
    #    print('-------------------------------------------------------------------------------------------------------')
        hemisphere_image_urls.append({'title': title.text, 'img_url': link})
    print(hemisphere_image_urls)

    listings['hemisphere_image_urls'] = hemisphere_image_urls

    browser.quit()

    return listings

# Create Mongo
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

listings = scrape()
print(listings)