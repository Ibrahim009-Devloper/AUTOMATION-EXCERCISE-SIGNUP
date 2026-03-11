import logging
import os
from datetime import datetime


class log_maker():
    @staticmethod
    def log_gen():

        logging.basicConfig(filename = ".//logs//Automation_excercise.log",level= logging.INFO,format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',datefmt='%Y-%m-%d %H:%M:%S',force=True)
       
        logger = logging.getLogger("Selenium logs Test")
        
        logger.setLevel(logging.INFO)
        return logger