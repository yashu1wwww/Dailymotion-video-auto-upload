from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

# Setup Chrome options (optional: headless, disable logs etc.)
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--headless")  # Optional for background mode

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

# Open Dailymotion login page
driver.get('https://www.dailymotion.com/signin')

# Accept cookies
try:
    accept_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.CookiePopup__button___2_4ue")))
    accept_btn.click()
except:
    print("Cookie popup not found or already accepted.")

# Login process
wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("motion1212@gmail.com")
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("motion#$%")
driver.find_element(By.XPATH, "//form//button").click()

# Navigate to upload page
wait.until(EC.url_contains("dailymotion.com"))
driver.get('https://www.dailymotion.com/upload')

# Upload video
video_path = r"C:\Users\yashw\Desktop\face\dailymotion success story part-1.mkv"
wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))).send_keys(video_path)

# Fill description
desc_box = wait.until(EC.presence_of_element_located((By.NAME, "description")))
desc_box.clear()
desc_box.send_keys("dailymotion success story part-1 video")

# Optional: Wait to visually confirm
time.sleep(20)

# Done
print("✅ Upload and description completed.")
# driver.close()  
