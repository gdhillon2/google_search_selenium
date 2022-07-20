from selenium import webdriver

from selenium.webdriver.chrome.service import Service

# imports keyboard keys like escape and enter
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# set up path and webdriver
ser = Service("/home/gurvir/chromedriver")
browser = webdriver.Chrome(service=ser)

# opens browser page
browser.get("https://google.com")

# finds search field and searches google
search = browser.find_element("name", "q")
search.send_keys("google")
search.send_keys(Keys.RETURN)

# find google searches
results = browser.find_elements(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']")

# prints google search result titles
for result in results:
	print(result.text)
