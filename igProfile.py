from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#---------------------LOGGER--------------------------------#
import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('igProfile')

class Profile():
    def __init__(self, obj):
        super().__init__()
        """
        Will open the profile and click on the last picture

        """
        obj.driver.find_element(By.XPATH, "//*[local-name()='nav' and contains(@class, 'NXc7H')]//a[img]").click()
        WebDriverWait(obj.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'g47SY' )))
        logger.info("Entramos al perfil")
        self.post = obj.driver.find_element_by_class_name('g47SY').text
        self.num = int(self.post)
        print(self.num)
        
        #self.maxNumPhotos = self.num
