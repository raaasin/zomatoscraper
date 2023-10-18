import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# List of Zomato restaurant URLs
restaurant_links = [
"https://www.zomato.com/visakhapatnam/siripuram-restaurants",
"https://www.zomato.com/visakhapatnam/waltair-uplands-restaurants",
"https://www.zomato.com/visakhapatnam/kirlampudi-layout-restaurants",
"https://www.zomato.com/visakhapatnam/mvp-colony-restaurants",
"https://www.zomato.com/visakhapatnam/maharani-peta-restaurants",
"https://www.zomato.com/visakhapatnam/jagadamba-junction-restaurants",
"https://www.zomato.com/visakhapatnam/dwaraka-nagar-restaurants",
"https://www.zomato.com/visakhapatnam/gajuwaka-restaurants",
"https://www.zomato.com/visakhapatnam/lawsons-bay-restaurants",
"https://www.zomato.com/visakhapatnam/maddilapalem-restaurants",
"https://www.zomato.com/visakhapatnam/asilmetta-restaurants",
"https://www.zomato.com/visakhapatnam/seethammadhara-restaurants",
"https://www.zomato.com/visakhapatnam/rushikonda-restaurants",
"https://www.zomato.com/visakhapatnam/marripalem-restaurants",
"https://www.zomato.com/visakhapatnam/sagar-nagar-restaurants",
"https://www.zomato.com/visakhapatnam/allipuram-restaurants",
"https://www.zomato.com/visakhapatnam/madhurawada-restaurants",
"https://www.zomato.com/visakhapatnam/ram-nagar-restaurants",
"https://www.zomato.com/visakhapatnam/balayya-sastri-layout-restaurants",
"https://www.zomato.com/visakhapatnam/nad-junction-restaurants",
"https://www.zomato.com/visakhapatnam/kancharapalem-restaurants",
"https://www.zomato.com/visakhapatnam/madhavadhara-restaurants",
"https://www.zomato.com/visakhapatnam/kurmannapalem-restaurants",
"https://www.zomato.com/visakhapatnam/akkayyapalem-restaurants",
"https://www.zomato.com/visakhapatnam/thagarapuvalasa-restaurants",
"https://www.zomato.com/visakhapatnam/bheemili-bheemunipatnam-restaurants",
"https://www.zomato.com/visakhapatnam/sriharipuram-restaurants",
"https://www.zomato.com/visakhapatnam/simhachalam-restaurants"
    # Add more restaurant URLs as needed
]

# Initialize lists to store data
all_urls = []
all_rest_name = []
all_ratings = []
all_price = []
all_cuisine = []
all_images = []

# Set up Selenium WebDriver
driver = webdriver.Chrome()

for link in restaurant_links:
    driver.get(link)
    time.sleep(2)

    scroll_pause_time = 1.8
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1

    while True:
        driver.execute_script("window.scrollTo(0, {0});".format(screen_height * i))
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if (screen_height) * i > scroll_height:
            break

    # Create a soup object
    soup = BeautifulSoup(driver.page_source, "html.parser")
    divs = soup.findAll('div', class_='jumbo-tracker')

    # Loop through restaurant divs and extract data
    for parent in divs:
        name_tag = parent.find("h4")
        if name_tag is not None:  # Check if the tag exists
            rest_name = name_tag.text

            link_tag = parent.find("a")
            base = "https://www.zomato.com"
            link = urljoin(base, link_tag.get('href'))

            image_tag = parent.find("img", class_="sc-s1isp7-5 fyZwWD")
            if image_tag:
                image_url = image_tag.get("src")
            else:
                image_url = None

            rating_tag = parent.div.a.next_sibling.div.div.div.div.div.div.div.text
            price_tag = parent.div.a.next_sibling.p.next_sibling.text
            cuisine_tag = parent.div.a.next_sibling.p.text

            all_urls.append(link)
            all_rest_name.append(rest_name)
            all_ratings.append(rating_tag)
            all_price.append(price_tag)
            all_cuisine.append(cuisine_tag)
            all_images.append(image_url)

# Create a DataFrame
df = pd.DataFrame({
    'links': all_urls,
    'names': all_rest_name,
    'ratings': all_ratings,
    'price for one': all_price,
    'cuisine': all_cuisine,
    'images': all_images
})

# Save restaurant data to a CSV file
df.to_csv("restaurant_data.csv")

# Close the WebDriver
driver.close()
