from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# loop for repeat the action

# the login information
username = input('enter the username:\n')
password = input('enter the password:\n ')
# variabl to stock location of chromdriver

driver = webdriver.Chrome()

# openthe site

driver.get('https://massar.men.gov.ma/Account')
try:
    wait =WebDriverWait(driver,4).until(
        EC.presence_of_element_located((By.NAME,'UserName'))
    )
finally:
    print('yeh')
    def logg (site,code):
        password = site.find_element(By.ID,'Password')
        password.clear()
        return password.send_keys(code)

    def log (site,user) :
         username = site.find_element(By.ID,'UserName')
         username.clear()
         return username.send_keys(user)
    def Enter (site) :
        button=site.find_element(By.ID,'btnSubmit')
        button.send_keys(Keys.ENTER)
# call the function to use
ussername = log(driver,username)
passord = logg(driver,password)
enter = Enter(driver)

    # close the driver
i =input('pause ? Y/N :\n')
while True :
    if i == 'y' or i == 'Y' :
        time.sleep(1)
        driver.close()
        break