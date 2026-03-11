import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from base_pages.signup_page import SignUp_page
from utilities.read_propertics import read_config
from utilities.custom_loger import log_maker




class Test_01_login_page():
    logger = log_maker.log_gen()
    
    
    


    def test_tittle_varification(self,setup):
        self.logger.info("Title Verificition started")
        self.driver = setup
        self.driver.get(read_config.get_admin_url())
        self.signup = SignUp_page(self.driver)
        self.signup.click_login_signup_btn()
        
        act_tittle = self.driver.title
        exp_tittle = "Automation Exercise - Signup / Login"

        if act_tittle == exp_tittle:
            assert True
            
        else:
            
            assert False
    def test_valid_signup(self,setup):
        self.logger.info("Signup test case started")
        self.driver = setup
        self.driver.get(read_config.get_admin_url())

        self.admin_lp =SignUp_page(self.driver)
        self.admin_lp.click_login_signup_btn()
        self.admin_lp.enter_your_name(read_config.get_User_name())
        self.admin_lp.enter_your_email()
        self.admin_lp.click_signup_btn()
        self.logger.info("******entered name and email sucessfully*****")
        
        email_exist_msg = self.admin_lp.email_alrady_exist()
        if email_exist_msg:
            self.driver.save_screenshot(".//scerennshots//Email_alrady_exist.png")
            self.logger.info("********Signup Faild. Email alrady exist*********")
            pytest.fail(f"Massage: {email_exist_msg}")
        

        self.logger.info("********Filling the information**********")
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
        self.logger.info("Account crerated sucessfully")
        if sucess_msg.strip()  != "ACCOUNT CREATED!":
            self.driver.save_screenshot(".//scerennshots//error_signup.png")
            self.logger.info("*******Account not created******")
            assert False
            
        self.logger.info("********The Test Case Has Been Passed*******")

        
        




    


