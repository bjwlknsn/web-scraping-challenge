import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import datetime as dt

# Create a function to initialize the webscraping browser with splinter 
def init_browser():
    # Establish chrome driver executable path. Make sure to define actual location on your drive.
    executable_path ={'executable_path': 'C:/Users/Us/chromedriver.exe'}
    # Open a splinter browser
    return Browser('chrome', **executable_path, headless=False)

# Create a callable function to scrape the data from the website    
def scrape(): 

    ### Initialize splitner broswer ###
    browser = init_browser()

    # Define the the URL
    url = 'https://mars.nasa.gov/news'

    # Visit the defined URL on splinter broswer
    browser.visit(url)

    # Create a BeautifulSoup object with the splinter broswer.html object and parse the html with 'html.parser'
    soup = bs(browser.html, 'html.parser')

    # Scrape the first instance of latest news title text and assign to a variable
    # Find the first article
    first_news_article = soup.find('li', class_="slide")

    # Find the title within that article summary and convert into .text and then .strip() of '/n'
    news_title = first_news_article.find('div', class_='content_title').text.strip()

    # Save the article link url
    article_link_string = first_news_article.find('a')['href']
    article_url = url + article_link_string

    # Scrape the first instance of latest paragraph text and assign to a variable
    # Find the paragraph within that article summary and convert into .text and then .strip() of '/n'
    news_p = first_news_article.find('div', class_="article_teaser_body").text.strip()

    # Open splinter browser to scrape the desired images
    # Define the URL path
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # Using the already established splinter engine, and open the url in broswer
    # Visit the defined URL on splinter broswer
    browser.visit(image_url)

    # delay action until browser loads
    time.sleep(1)

    # click on the sprinter browser link 'BaseImage' to see the image to store
    browser.find_by_css('img.BaseImage').click()
    time.sleep(1)

    html=browser.html
    soup=bs(html, 'html.parser')

    featured_image_url=soup.find('a', class_='BaseButton')['href']

    # Use Pandas to scrape the table information from the space-fact.com website on Mars
    # Define the url
    facts_url = 'https://space-facts.com/mars/'

    # Read html to get a list dataframes of all the tables
    tables = pd.read_html(facts_url)

    # Remove the first table from the list
    mars_facts_tbl = tables[0]

    # Name the columns
    mars_facts_tbl.columns = ['Attribute', 'Value']

    # Set the index to the Atrribute column
    mars_facts_tbl.set_index('Attribute', inplace=True)

    # Convert the dataframe into html
    html_mars_tbl = mars_facts_tbl.to_html()

    # Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
    # Define URL
    astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    root_usgs_url = 'https://astrogeology.usgs.gov/'

    # Use splinter browser to open url
    browser.visit(astro_url)

    # Create a BeautifulSoup object with the splinter broswer.html object and parse the html with 'html.parser'
    soup = bs(browser.html, 'html.parser')

    # Create an empty list to store dictonary values for the keys of 'img_url' and 'title'
    hemisphere_image_list = []

    # Parse the html and loop through to visit different webpages and scrape the data
    image_links = soup.find_all('div', class_='item')

    # Start the for loop
    for item in image_links:
            
        # Find the url link string from the 'a' tag and call the 'href' string
        link = item.find('a')['href']
           
        # Combine the root url from above and the link url
        combo_url = root_usgs_url + link
          
        # Open splinter browser using the combo_url link just created
        browser.visit(combo_url)
          
        # Let the browser load for 1 second before scraping data
        time.sleep(1)
         
        # Create BeautifulSoup object
        soup = bs(browser.html, 'html.parser')
            
        # Find the link to the image in the 'ul' tag, then the 'a' tag, and then call the second item 'href'
        # Store link string in variable 'image_link_hemi'
        image_link_hemi = soup.find('ul').find_all('a')[0]['href']
            
        # Find the title name using the 'h2' tag and class attribute 'title', and then pull the .text
        # Store title in variable 'title_text'
        title_text = soup.find('h2', class_='title').text
           
        # Append the hemisphere list with a dictionary of the keys and values
        hemisphere_image_list.append({
            'title': title_text, 
            'img_url': image_link_hemi
            })
            
        time.sleep(1)

    # Create a dictionary of all the web scraped data
    dict_mars_scrape = {
        'news_title': news_title,
        'news_p': news_p,
        'article_url': article_url,
        'featured_image_url': featured_image_url,
        'html_mars_tbl': html_mars_tbl,
        'hemisphere_image_list': hemisphere_image_list,
        # Add the time of the scrape to the dictionary
        'scrape_time': dt.datetime.now()
    }

    browser.quit()

    print(dict_mars_scrape)
    return dict_mars_scrape 
