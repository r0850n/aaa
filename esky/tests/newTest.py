
from common.loadDriver import LoadDriver_realDevice
import unittest, time, os
from appium import webdriver
from time import sleep
from pages.loader import Loader





class Android_esky_app(unittest.TestCase,Loader):
    "Class to run tests against the ATP WTA app"

    S3 = '4df13ae160004fe1'
    def setUp(self):
       
        self.driver = LoadDriver_realDevice.loadAppiumDriver()
        
       

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_esky_test(self):
        
        self.driver.implicitly_wait(30)
        time.sleep(5)
              
        self.get_Global_Methods().travel_from_to('Warszawa' , 'Katowice','Listopad 2015','10', "21")
         
        
        
        