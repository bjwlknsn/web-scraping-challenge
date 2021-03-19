# web-scraping-challenge

In this assignment I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step 1 - Scraping
I completed my initial scraping of the NASA Mars News (https://mars.nasa.gov/news/) and image gallery sites (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. Then I scraped a table of facts from the Space Facts site (https://space-facts.com/mars/). Finally, I scraped images of the hemispheres from USGS astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

## Step 2 - MongoDB and Flask Application
Next I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

See screenshots of the completed HTML page above in Mission_to_Mars/Screenshots.

If you want to run the code, remember to update the executable_path of the splinter browser to direct to the proper location of the chromedriver.exe on your conmputer.



