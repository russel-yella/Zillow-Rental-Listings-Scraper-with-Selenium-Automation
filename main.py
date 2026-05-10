import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#SELENIUM SETUP

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

#ZILLOW PAGE

zillow_url = "https://www.zillow.com/homes/for_rent/"

driver.get(zillow_url)

time.sleep(10)

soup = BeautifulSoup(driver.page_source, "html.parser")

#SCRAPE DATA

prices = soup.select("span[data-test='property-card-price']")
links = soup.select("a.property-card-link")
addresses = soup.select("address")

rents_prices = []
rents_links = []
rents_addresses = []

for price in prices:
    text = price.get_text(strip=True)

    match = re.search(r"\$[\d,]+", text)

    if match:
        rents_prices.append(match.group())

for link in links:
    href = link.get("href")

    if href:
        if href.startswith("/"):
            href = "https://www.zillow.com" + href

        rents_links.append(href)

for address in addresses:
    rents_addresses.append(" ".join(address.get_text().split()))

# Keep equal lengths
data = list(zip(rents_addresses, rents_prices, rents_links))

print(data)

# ------------------ GOOGLE FORM ------------------ #

form_url = "YOUR_GOOGLE_FORM_URL"

for address, price, link in data:

    driver.get(form_url)

    time.sleep(3)

    inputs = driver.find_elements(By.CSS_SELECTOR, "input")

    inputs[0].send_keys(address)
    inputs[1].send_keys(price)
    inputs[2].send_keys(link)

    submit_button = driver.find_element(
        By.XPATH,
        "//span[text()='Submit']"
    )

    submit_button.click()

    time.sleep(2)

driver.quit()