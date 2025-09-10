import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LinkedInEasyApplyBot:
    def __init__(self, config):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

        self.username = config["linkedin"]["username"]
        self.password = config["linkedin"]["password"]
        self.job_url = config["linkedin"]["job_url"]

    def login(self):
        self.driver.get(self.job_url)
        try:
            sign_in = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            sign_in.click()

            email_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            email_field.send_keys(self.username)

            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(self.password, Keys.ENTER)

            print("[INFO] Logged in successfully")

        except TimeoutException:
            print("[ERROR] Login failed")

    def start_easy_apply(self):
        try:
            easy_apply_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'jobs-apply-button')]"))
            )
            easy_apply_button.click()
            print("[INFO] Easy Apply clicked")

        except TimeoutException:
            print("[ERROR] Easy Apply button not found")

    def fill_application(self):
        try:
            # Example: answer a question field
            question_field = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
            )
            question_field.send_keys("1")

            # Example: check a radio button
            ready_option = self.driver.find_element(By.XPATH, "//fieldset//label[1]")
            ready_option.click()

            print("[INFO] Application form filled")

        except (TimeoutException, NoSuchElementException):
            print("[ERROR] Could not fill application")

    def review_and_submit(self):
        try:
            review_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label,'Review')]"))
            )
            review_button.click()
            print("[INFO] Review button clicked")

            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label,'Submit')]"))
            )
            submit_button.click()
            print("[INFO] Application submitted")

        except TimeoutException:
            print("[ERROR] Review/Submit button not found")

    def close(self):
        time.sleep(5)  # give time to see results
        self.driver.quit()


if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)

    bot = LinkedInEasyApplyBot(config)
    bot.login()
    bot.start_easy_apply()
    bot.fill_application()
    bot.review_and_submit()
    bot.close()