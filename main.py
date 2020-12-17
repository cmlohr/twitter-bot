from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

WEB_PAGE = "https://twitter.com/home"
DRIVER_PATH = "_your_driver_path_"
USER = "_twitter_user_name_"
PASSWORD = "_twitter_password_"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(WEB_PAGE)
print("connected to Twitter")
time.sleep(1)
print(">>> attempt to log in")
time.sleep(1)
print(">>> user input")
time.sleep(1)
user_input = driver.find_element_by_css_selector(
    "#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > "
    "form > div > div:nth-child(6) > label > div > "
    "div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x.r-1inuy60.r-ou255f.r-vmopo1 > div > input")
user_input.send_keys(USER)
print(">>> user entered")
time.sleep(1)
print(">>> password input")
time.sleep(1)
user_pass = driver.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
user_pass.send_keys(PASSWORD)
print(">>> password entered")
time.sleep(1)

user_pass.send_keys(Keys.ENTER)
print("wait...")
time.sleep(5)
print(">>> log in successful")

print(">>> compose tweet")
tweet = driver.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                  /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                  /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                  /div/div/div''')
tweet.send_keys("└[∵┌]└[ ∵ ]┘[┐∵]┘")

print(">>> click tweet")
time.sleep(2)
tweet_btn = driver.find_element_by_css_selector(
    "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > "
    "div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-atwnbb > div:nth-child(1) > div > div > "
    "div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > "
    "div:nth-child(4) > div > div > div:nth-child(2) > "
    "div.css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1n0xq6e.r-1vuscfd.r-1dhvaqw"
    ".r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr")
tweet_btn.click()
print(">>> tweet sent")

driver.quit()

