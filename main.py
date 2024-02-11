from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

PROMISED_DOWN = 20
PROMISED_UP = 20
TWITTER_EMAIL = 'fakeofawwab@gmail.com'
TWITTER_PASSWORD = '&zwj2xGe)XsC,%v'

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.find_element(By.CLASS_NAME, 'start-text').click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)
        print(f"Download Speed: {self.down}\nUpload Speed: {self.up}")



if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()