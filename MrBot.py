from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, signal
from time import sleep
import sys


userId = '*****'
passCode = '*******'
nobill = '$0.00'


browser = webdriver.Chrome(executable_path= 'C:/Users/Kenneth/Documents/Python/chromedriver.exe')
browser.get('https://www.firstenergycorp.com/content/customer/log_in.html')


#fill in username and password
username = browser.find_element_by_id('loginUsername')
username.send_keys(userId)
password = browser.find_element_by_id('loginPwd')
password.send_keys(passCode)

#click Submit button
submit = browser.find_element_by_name('primaryButton')
submit.click()


# click paybill method
paybill = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='btn btn-primary']")))
paybill.click();

# Extract bill amount
price = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='pay-box active']/p"))).text
electricBillAmount = price[1:]
if price == nobill:
    print(f"Your bill amount is {price}.")
    sleep(10) 
    os.system("taskkill /im chrome.exe /f")
    os.kill(os.getpid(), signal.SIGTERM)
      
   

#Enter bill amount
billAmount = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "payAmount")))
billAmount.send_keys(electricBillAmount)

#Enter and review payment
checkAgreementBox = browser.find_element_by_id('terms')
checkAgreementBox.click()

#review payment
reviewPayment = browser.find_element_by_name('reviewBeforePaying')
reviewPayment.click()

#Submit payment and close window
paybill = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='btn btn-primary']")))
paybill.click();
sleep(3)
os.system("taskkill /im chrome.exe /f")
os.kill(os.getpid(), signal.SIGTERM)




