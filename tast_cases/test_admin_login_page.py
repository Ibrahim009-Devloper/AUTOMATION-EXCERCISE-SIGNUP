import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from base_pages.signup_page import SignUp_page
from utilities.read_propertics import read_config


class Test_01_login_page():
    
    


    def test_tittle_varification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(read_config.get_admin_url())
        act_tittle = self.driver.title
        exp_tittle = "Automation Exercise - Signup / Login"

        if act_tittle == exp_tittle:
            assert True
            self.driver.quit()
        else:
            self.driver.quit()
            assert False
    def test_valid_signup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(read_config.get_admin_url())

        self.admin_lp =SignUp_page(self.driver)
        self.admin_lp.enter_your_name(read_config.get_User_name())
        self.admin_lp.enter_your_email()
        self.admin_lp.click_signup_btn()
        
        email_exist_msg = self.admin_lp.email_alrady_exist()
        if email_exist_msg:
            pytest.fail(f"Massage: {email_exist_msg}")
            self.driver.close()
        


        self.admin_lp.select_gender()
        self.admin_lp.signup_get_password(read_config.get_password())
        self.admin_lp.signup_select_days(read_config.get_Days())
        self.admin_lp.singup_select_month(read_config.get_month())
        self.admin_lp.signup_select_years(read_config.get_year())
        self.admin_lp.click_signup_checkbox()
        self.admin_lp.signup_first_name(read_config.get_frist_name())
        self.admin_lp.signup_last_name(read_config.get_last_name())
        self.admin_lp.signup_company_name(read_config.get_company_name())
        self.admin_lp.signup_address1(read_config.get_address1())
        self.admin_lp.signup_address2(read_config.get_address2())
        self.admin_lp.signup_country(read_config.get_contry_name())
        self.admin_lp.signup_state(read_config.get_state_name())
        self.admin_lp.signup_city(read_config.get_city_name())
        self.admin_lp.signup_zipcode(read_config.get_zipcode())
        self.admin_lp.signup_mobile_number(read_config.get_phone_number())
        self.admin_lp.click_create_account_btn()

        sucess_msg = self.admin_lp.Account_create_sucessfully()
        if sucess_msg.strip()  != "ACCOUNT CREATED!":
            self.driver.save_screenshot(".//scerennshots//error_signup.png")
            self.driver.quit()
            assert False

        
        self.driver.quit()




    


