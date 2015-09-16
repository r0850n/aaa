
from common.loadDriver import LoadDriver_realDevice
import unittest, time, os
from appium import webdriver
from time import sleep
from pages.loader import Loader
from ddt import ddt, data, file_data, unpack
from appium.webdriver.common.touch_action import TouchAction
import json
from pprint import pprint


@ddt
class Android_esky_app(unittest.TestCase,Loader):
    "Class to run tests against the ATP WTA app"

    S3 = '4df13ae160004fe1'
    def setUp(self):
       
        self.driver = LoadDriver_realDevice.loadAppiumDriver()
         #desired_caps = LoadDriver_realDevice.get_desired_capabilities('com.esky.apk')
         #self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
       
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
       # self.driver = LoadDriver_realDevice.loadAppiumDriver()
         
    @file_data('bbb.json')
    def test_esky_test(self,data):
        
        self.driver.implicitly_wait(30)
        time.sleep(5) 
        try:
            self.get_Global_Methods().travel_from_to(data["from"] , data["to"],data["month"],data["date1"], data["date2"])
        except:
            self.get_Welcome_Page().PL().click()
            self.get_Global_Methods().travel_from_to(data["from"] , data["to"],data["month"],data["date1"], data["date2"])
        
        #self.driver.quit()
        
        