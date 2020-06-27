from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import platform 
import os

#---------------------LOGGER--------------------------------#
import logging
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('root')

class  startChrome():
    def __init__(self):
        super().__init__()
        #Open chrome
        #path_driver = os.path.dirname(os.path.realpath(__file__))
        if(platform.system() == 'Windows'):
            self.driver = webdriver.Chrome("./chrome/chromedriver.exe" )
        elif(platform.system()== 'Linux'):
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Chrome("./chrome/chromedriver")
        logger.warning("This code was excecuted from {}".format(platform.system()))

        self.driver.get("https://instagram.com")
        self.username = 'photoandtravel2020'
        self.password = 'mannheimzittau'
        self.user = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(self.username)
        self.pas = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys(self.password + Keys.ENTER)
        logger.info("Acces Granted")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'Instagram')]"))).click()


Bot = startChrome()
