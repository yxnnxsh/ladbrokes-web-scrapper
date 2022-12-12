from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Changing ChromeDriver Defualt Options

# Creates an isntance of the Options class
options = Options()
# Turns on the headless
options.headless = True
options.add_argument('window-size=1920x1080') #Headless = true





# website url
web = 'https://www.ladbrokes.com.au/'
# path where we downloaded chromedriver
path = '/Users/yannihaddad/Desktop/betting/chromedriver'
# 
driver = webdriver.Chrome(path)
driver.get(web)

