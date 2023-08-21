from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

CHROMEDRIVER_PATH = "C:\\Users\\mayanja4\\chromedriver\\chromedriver.exe"
SERVICE = Service(executable_path=CHROMEDRIVER_PATH)
SIMILAR_ACCOUNT = "account whose followers you want"
USERNAME = "your fb login username"
PASSWORD = "your fb password"


class InstaFollower:

    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)

    def login(self, user, password):
      '''login with facebook account'''
        self.driver.get("https://www.instagram.com/")
        time.sleep(1)
        login = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[5]/button")
        login.click()
        time.sleep(1)
        user_ = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input")
        user_.send_keys(user)
        pas_= self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input")
        pas_.send_keys(password)
        pas_.send_keys(Keys.ENTER)
        time.sleep(15)
        notification = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        notification.click()

    def find_followers(self, target):
        self.driver.get(f"https://www.instagram.com/{target}/followers")
        time.sleep(3)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(1):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        while True:
            try:

                list_of_people = self.driver.find_elements(By.CSS_SELECTOR, 'button')
                print(len(list_of_people))
                for person in list_of_people:
                    print(person.text)
                    if person.text == "Follow":
                        time.sleep(random.randint(1000, 1600) / 1000)
                        person.click()
                        time.sleep(random.randint(5, 10))
                    print(len(list_of_people))
                print('Scrolling...')

                fBody = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
                scroll = 0
                while scroll < 5:  # scroll 5 times, feel free to change this
                    self.driver.execute_script(
                        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                    time.sleep(2)
                    scroll += 1


            except Exception as e:
                print(e)


instafollower = InstaFollower(SERVICE)

instafollower.login(USERNAME, PASSWORD)
instafollower.find_followers(SIMILAR_ACCOUNT)
instafollower.follow()

instafollower.driver.quit()
