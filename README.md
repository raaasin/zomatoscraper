# Zomato Scraper

## Overview

The **Zomato Scraper** is a Python script for web scraping restaurant data from the Zomato website. It collects information such as restaurant names, ratings, price ranges, cuisines, images, addresses, and latitude-longitude coordinates. This data can be useful for various purposes, including data analysis, restaurant recommendations, or other applications.

## Prerequisites

Before using the Zomato Scraper, make sure you have the following dependencies and setup:

1. Python: Ensure that you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Python Libraries: Install the required Python libraries using `pip` by running the following command:

   ```bash
   pip install pandas selenium beautifulsoup4
   ```

3. Selenium WebDriver: You need to download the appropriate Selenium WebDriver for your web browser (e.g., ChromeDriver for Google Chrome). Ensure that the WebDriver is in your system's PATH or specify its location in the script.
4. Web Browser: The script currently uses Google Chrome. Make sure you have Google Chrome installed on your system.

## Usage

1. Clone the Repository:

   ```bash
   git clone https://github.com/raaasin/zomatoscraper.git
   cd zomatoscraper
   ```
2. Prepare Restaurant URLs:

   Modify the `restaurant_links` list in the `zommy.py` script to include the Zomato restaurant URLs you want to scrape.
3. Run the Script:

   Execute the script using the following command:

   ```bash
   python zommy.py
   ```
4. Output:

   The script will scrape restaurant data and save it to a CSV file named 'restaurant_data.csv' within the same directory.

   Additionally, it will extract location data (address, latitude, and longitude) and save it to 'scraped_data.csv'.

## Customize and Extend

Feel free to customize the script and extend its functionality to meet your specific needs. You can add more data fields, error handling, or any other features to enhance the scraping process.

## Disclaimer

Please be aware of the terms of use and legal restrictions when scraping data from websites. Ensure that your use of this script complies with Zomato's terms and conditions and applicable laws and regulations.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy scraping! If you have any questions or encounter issues, feel free to reach out for support or improvements.
