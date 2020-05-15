from selenium import webdriver
import time

chrome_browser = webdriver.Chrome(executable_path='/home/aman909/Desktop/chromedriver')
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(10)