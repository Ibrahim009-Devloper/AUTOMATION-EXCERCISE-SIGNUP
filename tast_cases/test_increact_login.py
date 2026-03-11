from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pytest
from base_pages.incarect_login import Increate_login
from utilities.custom_loger import log_maker
from utilities.read_propertics import read_config



class Test_increact_login():
    logger = log_maker.log_gen()
    

    def test_home_page_title_varification(self,setup):
        self.logger.info("******home page title verification test started*******")
        self.driver = setup
        self.driver.get(read_config.get_admin_url())
        act_title = self.driver.title
        exp_title = "Automation Exercise"
        assert act_title == exp_title,"Title isn't matching. chake the code"
        self.logger.info("********home page title verification finished********")

    

    def test_increact_login(self,setup):
        self.logger.info("******increact login test started*******")
        self.driver = setup
        self.driver.get(read_config.get_admin_url())
        
        self.login = Increate_login(self.driver)
        self.login.click_login_signup_btn()
        el = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'login-form')]//h2")))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",el)
        assert el.is_displayed(),"the test is not displayed"
        self.logger.info("*******Login to your account is verified********")
        self.login.incrate_login_email()
        self.login.increact_password(read_config.get_password())
        self.login.click_login_btn()
        error_masg = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,"//p[contains(normalize-space(),'incorrect!')]")))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",error_masg)
        assert error_masg.is_displayed(),"Error massage is not displayed"
        self.logger.info("*******Error massage is verified********")
        



