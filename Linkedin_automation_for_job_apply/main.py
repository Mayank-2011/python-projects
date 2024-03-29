# This automation is for jobs which require only your phone number and resume no other things that you need to specify alternatively
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

LINKEDIN_USERNAME = "linkedin username or email"
LINKEDIN_PASSWORD = "linkedin password"
PHONE = "your mobile number"

chromedriver = "chromedriver.exe path on your machine"
service = Service(executable_path=chromedriver)
driver = webdriver.Chrome(service=service)

driver.get("job url with easy apply option tagged")
time.sleep(2)
sign_in = driver.find_element(By.LINK_TEXT, "Sign in").click()
username = driver.find_element(By.ID, "username")
username.send_keys(LINKEDIN_USERNAME)
password = driver.find_element(By.ID, "password")
password.send_keys(LINKEDIN_PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(1)

all_listings = driver.find_elements(By.CLASS_NAME,"job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("aria-label") == "Continue to next step":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
