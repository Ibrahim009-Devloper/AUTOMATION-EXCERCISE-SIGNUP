from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
import time


class Increate_login():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)
        verifi_home_page_el = (By.XPATH,"")
        self.click_login_el = (By.XPATH,"//a[contains(text(),' Signup / Login')]")
        self.email_el = (By.NAME,"email")
        self.password_el = (By.NAME,"password")
        self.click_login_btn_el = (By.XPATH,"//button[contains(@data-qa,'login-button')]")
        

    def click_login_signup_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.click_login_el)).click()

    def generate_random_email(self):
        leanth = 8
        username = "".join(random.choices(string.ascii_lowercase+string.digits,k=leanth))
        domain = random.choice(["gmail.com","yahoo.com","mail.com","email.com","local.com"])
        return f"{username}@{domain}"



    def incrate_login_email(self):
        random_email = self.generate_random_email()
        email = self.wait.until(EC.visibility_of_element_located(self.email_el))
        email.clear()
        email.send_keys(random_email)

    def increact_password(self,password):
        pwd = self.wait.until(EC.visibility_of_element_located(self.password_el))
        pwd.clear()
        pwd.send_keys(password)
    
    def click_login_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.click_login_btn_el)).click()





        


    