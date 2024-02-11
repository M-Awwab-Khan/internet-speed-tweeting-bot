from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

PROMISED_DOWN = 16
PROMISED_UP = 16
TWITTER_EMAIL = 'fakeofawwab@gmail.com'
TWITTER_PASSWORD = '&zwj2xGe)XsC,%v'

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')



if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()