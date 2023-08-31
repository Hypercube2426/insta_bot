from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# Taking URL from the user
url = input("Enter the URL: ")

# Using Requests and Beautiful Soup to scrape the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Using Selenium to interact with the webpage (optional)
driver = webdriver.Chrome()  # You'll need to have chromedriver installed and in your PATH
driver.get(url)

# You can perform various interactions using Selenium here
# For example: driver.find_element_by_id('element_id').click()

# Close the Selenium webdriver
driver.quit()
