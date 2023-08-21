from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import smtplib

PROMISED_DOWN = "your promised download speed"
PROMISED_UP = "your promised upload speed"
CHROMEDRIVER_PATH = "chromedriver.exe path"
SERVICE = Service(executable_path=CHROMEDRIVER_PATH)


class InternetSpeedTwitterBot:

    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        accept_cookies = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[2]/div[1]/div/button")
        accept_cookies.click()
        go_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        time.sleep(1)
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        print(f"down: {self.down}\nup: {self.up}")


    def mail_at_provider(self):
        message = f"Hey, why my internet speed is {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up."
        email = "your email"
        password ="your application password"
        with smtplib.SMTP("SMTP server", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs="your isp's complaint email",
                msg=f"Subject:Internet speed less than promised\n\n{message}"
            )





internet_speed_bot = InternetSpeedTwitterBot(SERVICE)

internet_speed_bot.get_internet_speed()

internet_speed_bot.mail_at_provider()
