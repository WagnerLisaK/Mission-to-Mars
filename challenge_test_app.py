# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'

# 1. Use browser to visit the URL 
site_url = 'https://marshemispheres.com/'

browser.visit(site_url)
html = browser.html
html_soup = soup(html, 'html.parser')

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
hemisphere_info = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.


# Defines "items" to a smaller portion of the page in order to retrieve the titles.
items = html_soup.find('div', class_='collapsible results')

# Creates each hemisphere's url
hrefs = []
unique_hrefs = []
page_urls = []
    
a = items.find_all('a', class_= 'itemLink product-item')
 
for x in a:
    hrefs.append(x['href'])
     
for x in hrefs:
    if x not in unique_hrefs:
        unique_hrefs.append(x)
        page_url = f'https://marshemispheres.com/{x}'
        page_urls.append(page_url)
#print("Page_URLS = " + str(page_urls))
   

# Visits each each hemisphere's page and retrieves the image url and store
# the url in a list
img_urls = []

for page_url in page_urls:
    browser.visit(page_url)
    
    page_html = browser.html
    page = soup(page_html, "html.parser")
   
    dnlds = page.find('div', class_='downloads')
    a = dnlds.find('a')
        
    img_href = a['href']
    img_url = f'https://marshemispheres.com/{img_href}'
    #img_urls.append(img_url)
    
    cover = page.find('div', class_="cover")
    title = cover.find("h2", class_="title").text
    print(img_url)
    print(title)
    
    wait = input()
    
    dictionary = {img_url, title}
    print(dictionary)
    hemisphere_image_urls.append(dictionary)

    wait = input()

    # 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()




