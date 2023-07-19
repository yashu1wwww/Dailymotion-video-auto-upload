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
driver.get("https://www.dailymotion.com/dm/partner/sign-in") 
time.sleep(5)
driver.find_element_by_name("username").send_keys("dailytell23@gmail.com") #replace with your email
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/main/div/main/form/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/main/div/main/form/div/div[2]/span/input').send_keys("Daily@#$%") #replace with your password
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/main/div/main/form/div/button').click()
time.sleep(7)
#driver.find_element_by_css_selector("#react-root > div > header > div.src-common-layouts-global-nav-index__cellTopRight--13_FD > div.src-app-wrapper__createContentMenuButton--FBBxc.popoverMode > svg").click()
#driver.find_element_by_xpath('//*[@id="scrollable"]/span/span/button').click()
driver.find_element_by_xpath('//*[@id="scrollable"]/span/span/button/span').click()
#driver.find_element_by_css_selector("#scrollable > span > span > button > span").click()
#driver.find_element_by_css_selector("#scrollable > span > span > button").click()
#driver.find_element_by_xpath('//*[@id="react-root"]/div/div/main/div/div/div/div/div/div[2]/span[2]
#driver.find_element_by_css_selector("#react-root > div > div > main > div > div > div > div > div > div.src-routes-media-common-components-empty-list-index__root--38xIj > span.src-routes-media-common-components-empty-list-index__link--2hCRT").click()
#driver.find_element_by_xpath('//*[@id="react-root"]/div/div/main/div/div/div/div/div/div[2]/span[2]/a').click()
#driver.find_element_by_xpath('//*[@id="react-root"]/div/div/main/div/div/div/div/div/div[2]/span[2]/a').click()
#driver.find_element_by_xpath('//*[@id="react-root"]/div/div/main/div/div/div/div/div/div[2]/span[2]').click()
#driver.find_element_by_css_selector("#react-root > div > div > main > div > div > div > div > div > div.src-routes-media-common-components-empty-list-index__root--38xIj > span.src-routes-media-common-components-empty-list-index__link--2hCRT > a > span").click()
#driver.find_element_by_xpath('//*[@id="react-root"]/div/div/main/div/div/div/div/div/div[2]/span[2]/a/span').click()
time.sleep(3)
driver.find_element_by_xpath('//input[@type="file"]').send_keys(r"C:\Users\Hp\Desktop\nest\videos\video is good.mp4") #path of the video where you want you upload
time.sleep(13)
# Submit the upload form
submit_button = driver.find_element_by_id("submit_button_id")
submit_button.click()
time.sleep(10)