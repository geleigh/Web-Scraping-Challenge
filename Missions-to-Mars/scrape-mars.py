#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install splinter


# In[22]:


from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser
from pprint import pprint
from datetime import datetime
import requests
import time


# # MARS NEWS

# In[23]:


# url
url = 'https://mars.nasa.gov/news/'


# In[24]:


# Retrieve page with the requests module
response = requests.get(url)


# In[25]:


# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')


# In[26]:


# Executable Path/Initialize Browser
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[27]:


# Scrape the Latest News Title
news_title = soup.find("div", class_="content_title").get_text()
print(news_title)

# Scrape the Latest Paragraph Text
news_p = soup.find("div", class_="rollover_description_inner").get_text()
print(news_p)


# # MARS IMAGES

# In[51]:


# JPL Mars Space Images - Featured Image

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[52]:


## Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

full_image_button = browser.find_by_id("full_image")
full_image_button.click()


# In[53]:


# Find More Info button to click
browser.is_element_present_by_text("more info", wait_time=1)
more_info = browser.find_link_by_partial_text("more info")
more_info.click()


# In[54]:


# Parse Results HTML with BeautifulSoup
html = browser.html
image_soup = BeautifulSoup(html, "html.parser")


# In[59]:


# Image URL
img_url = image_soup.select_one("figure.lede a img").get("src")
featured_image_url=(url + img_url)
print(featured_image_url)


# # MARS WEATHER

# In[88]:


## 

html = requests.get("https://twitter.com/marswxreport?lang=en").text
weather_soup = BeautifulSoup(html, "html.parser")

try:
    tweet = weather_soup.find_all('div', class_="js-tweet-text-container")
    i = 0
    for tweets in tweet:
        if "InSight" in tweet[i].text:
            print("mars_weather = " + tweet[i].text.split("pic")[0])
            break
        i += 1
except:
    print("tweet not found")


# # MARS FACTS

# In[95]:


# Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
mars_df = pd.read_html("https://space-facts.com/mars/")[0]
# print(mars_df)
# Use Pandas to convert the data to a HTML table string.
mars_df.columns=["Mars Facts", "Data"]
print(mars_df.to_html())


# # MARS HEMISPHERES

# In[96]:


# Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[101]:


hemisphere_image_urls = []

# Get a List of All the Hemispheres
links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    browser.find_by_css("a.product-item h3")[item].click()
    sample_element = browser.find_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # Add Hemisphere URL to List
    hemisphere_image_urls.append(hemisphere)
    
    # Go Back
    browser.back()
    
hemisphere_image_urls


# In[ ]:




