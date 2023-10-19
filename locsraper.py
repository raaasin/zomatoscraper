import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Read the CSV file containing the links
df = pd.read_csv('zomtrue.csv')

# Initialize a list to store the scraped data
data = []

# Initialize a Selenium WebDriver (you need to download the appropriate WebDriver for your browser)
driver = webdriver.Chrome()

# Iterate through each link in the CSV
for link in df['links']:
    # Modify the link to remove the '/order' part
    cleaned_link = link.split('/order')[0]

    # Visit the cleaned link
    driver.get(cleaned_link)

    try:
        # Wait for the page to load (you may need to adjust the time based on your internet speed)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[starts-with(@href, "https://www.google.com/maps/dir/?api=1&destination=")]')))

        # Scroll down the page
        driver.execute_script("window.scrollBy(0, 500)")

        # Wait for the page to fully load (you may need to adjust the time)
        driver.implicitly_wait(1)

        # Find the anchor tag with the specific href attribute
        anchor_element = driver.find_element_by_xpath('//a[starts-with(@href, "https://www.google.com/maps/dir/?api=1&destination=")]')

        # Extract the href attribute
        href = anchor_element.get_attribute("href")

        # Extract latitude and longitude from the href attribute
        if "destination=" in href:
            coordinates = href.split('destination=')[1]
            latitude, longitude = map(float, coordinates.split(','))
        else:
            latitude, longitude = None, None

        # Find the address element
        address_element = driver.find_element_by_css_selector('p.sc-1hez2tp-0.clKRrC')
        address = address_element.text

        data.append({
            'Links': link,
            'Address': address,
            'Latitude': latitude,
            'Longitude': longitude
        })
    except:
        # Handle the timeout or other exceptions
        data.append({
            'Links': link,
            'Address': 'Timeout or Error',
            'Latitude': None,
            'Longitude': None
        })

# Close the Selenium WebDriver
driver.quit()

# Create a new DataFrame from the collected data
new_df = pd.DataFrame(data)

# Save the new DataFrame to a CSV file
new_df.to_csv('scraped_data.csv', index=False)

# Print the first few rows of the new DataFrame
print(new_df.head())
