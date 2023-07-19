from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  
driver.get('https://www.dailymotion.com/signin')

time.sleep(3)

driver.find_element_by_css_selector("#root > div > div.CookiePopup__desktopContainer____u4u4 > button").click()

time.sleep(2)

driver.find_element_by_name("email").send_keys("motion1212@gmail.com") #replace with your dailymotion email

time.sleep(2)

driver.find_element_by_name("password").send_keys("motion#$%") #replace with your dailymotion password

time.sleep(3)

driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/form/div/button').click()

time.sleep(3)

# Navigate to the upload page
driver.get('https://www.dailymotion.com/upload')

time.sleep(6)

driver.find_element_by_xpath('//input[@type="file"]').send_keys(r"C:\Users\yashw\Desktop\face\dailymotion success story part-1.mkv") #path of the video where your video located

time.sleep(4)

driver.find_element_by_name("description").send_keys("dailymotion success story part-1 video") #change description to your video whats need..

time.sleep(20)

#in upcoming days i will try to update the category auto select others reamining things after decription or if you know means fork it...



