import configparser
import os


config = configparser.RawConfigParser()
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(base_dir)
config_path = os.path.join(project_root,"configarations","config.ini")
config.read(config_path)

class read_config():
    @staticmethod
    def get_admin_url():
        url = config.get('signup all element info','url')
        return url
    
    # @staticmethod
    # def get_email_address():
    #     Email = config.get('signup all element info','email')
    #     return Email
    
    @staticmethod
    def get_User_name():
        Name = config.get('signup all element info','Name')
        return Name
    
    @staticmethod
    def get_password():
        Password = config.get('signup all element info','Password')
        return Password
    
    @staticmethod
    def get_Days():
        day = config.get('signup all element info','Days')
        return day
    
    @staticmethod
    def get_month():
        month = config.get('signup all element info','Month')
        return month
    
    @ staticmethod
    def get_year():
        year = config.get('signup all element info','year')
        return year
    
    @staticmethod
    def get_frist_name():
        name = config.get('signup all element info','Frist_name')
        return name
    
    @staticmethod
    def get_last_name():
        name = config.get('signup all element info','last_name')
        return name
    
    @staticmethod
    def get_company_name():
        compani = config.get('signup all element info','company')
        return compani
    
    @staticmethod
    def get_address1():
        address = config.get('signup all element info','Address1')
        return address
    
    @staticmethod
    def get_address2():
        address = config.get('signup all element info','Address2')
        return address
    
    @staticmethod
    def get_contry_name():
        contry = config.get('signup all element info','Country')
        return contry
    
    @staticmethod
    def get_state_name():
        state = config.get('signup all element info','State')
        return state
    
    @staticmethod
    def get_city_name():
        city = config.get('signup all element info','city')
        return city
    
    @staticmethod
    def get_zipcode():
        zipcode = config.get('signup all element info','Zipcode')
        return zipcode
    
    @staticmethod
    def get_phone_number():
        number = config.get('signup all element info','Phone_number')
        return number

