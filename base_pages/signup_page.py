from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
# for random genarate email
import string
import random




class SignUp_page():
    testbox_username_input_el = (By.NAME,"name")
    testbox_email_input_el = (By.XPATH,"//input[contains(@data-qa,'signup-email')]")
    signup_btn_el = (By.XPATH,"//button[contains(@data-qa,'signup-button')]")
    #if email already exist element
    signup_email_alrady_exist_el = (By.XPATH,"//p[contains(text(),'Email Address already exist!')]")
    signup_tittle_el = (By.ID,"id_gender1")
    signup_password_el = (By.ID,"password")
    signup_date_el = (By.ID,"days")
    signup_month_el = (By.ID,"months")
    singup_year_el = (By.ID,"years")
    signup_checkbox_el = (By.ID,"newsletter")
    # Adderess informations
    signup_frist_name_el = (By.ID,"first_name")
    signup_last_name_el = (By.ID,"last_name")
    signup_company_name_el = (By.ID,"company")
    signup_address1_el = (By.ID,"address1")
    signup_address2_el = (By.ID,"address2")
    signup_select_country_el =(By.ID,"country")
    signup_state_el = (By.ID,"state")
    signup_city_el = (By.ID,"city")
    signup_zipcode_el = (By.ID,"zipcode")
    signup_phone_number_el = (By.ID,"mobile_number")
    signup_click_create_account_btn = (By.XPATH,"//button[contains(@data-qa,'create-account')]")

    #Account created sucessfully massage locator
    signup_sucessfully_el = (By.XPATH,"//h2[contains(@data-qa,'account-created')]//b")



    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,30)

    def enter_your_name(self,Name:str):
        name = self.wait.until(EC.visibility_of_element_located(self.testbox_username_input_el))
        name.clear()
        name.send_keys(Name)

    def random_email(self):
        leanth = 8 
        username = "".join(random.choices(string.ascii_lowercase + string.digits, k = leanth))
        domain = random.choice(["gmail.com","yahoo.com","outlook.com","example.com"])
        return f"{username}@{domain}"

    def enter_your_email(self):
        email = self.wait.until(EC.visibility_of_element_located(self.testbox_email_input_el))
        email.clear()
        email.send_keys(self.random_email())

    def click_signup_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_btn_el)).click()

    # if email address is alrady exist then
    def email_alrady_exist(self):
        try:
            massage_test = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located(self.signup_email_alrady_exist_el)).text
            return massage_test
        except TimeoutException:
            return None

    def select_gender(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_tittle_el)).click()

    def signup_get_password(self,password):
        pwd = self.wait.until(EC.visibility_of_element_located(self.signup_password_el))
        pwd.clear()
        pwd.send_keys(password)

    def signup_select_days(self,days:str):
        date = self.wait.until(EC.presence_of_element_located(self.signup_date_el))
        select = Select(date)
        select.select_by_visible_text(days)

    def singup_select_month(self,Month: str):
        month = self.wait.until(EC.presence_of_element_located(self.signup_month_el))
        select = Select(month)
        select.select_by_visible_text(Month)

    def signup_select_years(self,years: str):
        year = self.wait.until(EC.presence_of_element_located(self.singup_year_el))
        select = Select(year)
        select.select_by_visible_text(years)

    def click_signup_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_checkbox_el)).click()

    # Address informations area

    def signup_first_name(self,Name:str):
        name = self.wait.until(EC.visibility_of_element_located(self.signup_frist_name_el))
        name.clear()
        name.send_keys(Name)

    def signup_last_name(self,Name:str):
        name = self.wait.until(EC.visibility_of_element_located(self.signup_last_name_el))
        name.clear()
        name.send_keys(Name)

    def signup_company_name(self,Company:str):
        company = self.wait.until(EC.visibility_of_element_located(self.signup_company_name_el))
        company.clear()
        company.send_keys(Company)

    def signup_address1(self,Address:str):
        address = self.wait.until(EC.visibility_of_element_located(self.signup_address1_el))
        address.clear()
        address.send_keys(Address)

    def signup_address2(self,Address:str):
        address = self.wait.until(EC.visibility_of_element_located(self.signup_address2_el))
        address.clear()
        address.send_keys(Address)
    
    def signup_country(self,Country:str):
        country = self.wait.until(EC.presence_of_element_located(self.signup_select_country_el))
        select = Select(country)
        select.select_by_visible_text(Country)

    def signup_state(self,State:str):
        self.wait.until(EC.visibility_of_element_located(self.signup_state_el)).send_keys(State)

    def signup_city(self,City:str):
        self.wait.until(EC.visibility_of_element_located(self.signup_city_el)).send_keys(City)

    def signup_zipcode(self,Zipcode:str):
        self.wait.until(EC.visibility_of_element_located(self.signup_zipcode_el)).send_keys(Zipcode)
    
    def signup_mobile_number(self,Phone_number:str):
        self.wait.until(EC.visibility_of_element_located(self.signup_phone_number_el)).send_keys(Phone_number)

    def click_create_account_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_click_create_account_btn)).click()

    def Account_create_sucessfully(self):
        text = self.wait.until(EC.visibility_of_element_located(self.signup_sucessfully_el)).text
        return text


    

    


    