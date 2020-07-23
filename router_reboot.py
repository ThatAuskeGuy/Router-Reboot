import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Sets option to run Chrome headless
options = Options()
options.headless = True

# Opens Chrome to router's page, then logs in
print('Getting ready to restart router')

driver = webdriver.Chrome(".\chromedriver", options=options)
driver.get("your_router_address_here")

inputAccessCode = driver.find_element_by_id("ADM_PASSWORD")
inputAccessCode.send_keys("your_access_key_here")
inputAccessCode.submit()

# Function that creates a countdown timer
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def is_connected():
    while True:
        try:
            urllib.request.urlopen('http://www.google.com')
            print('Reestablished internet connection')
            break
        except urllib.error.URLError:
            print('No internet connection yet. Checking again in:')
            countdown(5)

        

# Warns user that the router is about to restart, then at the end of the timer, restarts router then closes Chrome
print('\nRESTARTING ROUTER IN:')
countdown(60)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'RESTART'))).click()

driver.close()

print('RESTARTING ROUTER: Please be patient')
print('Begining checks for internet connectivity in:')
countdown(10)
is_connected()
