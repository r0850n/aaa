from common.loadDriver import LoadDriver_realDevice
__author__ = 'robert'


import unittest, time, os
from appium import webdriver
from time import sleep
from pages.pageLocators import Global_Methods, Home_Page, Airports_search



class Android_esky_app(unittest.TestCase):
    "Class to run tests against the ATP WTA app"

    S3 = '4df13ae160004fe1'
    def setUp(self):
       
        self.driver = LoadDriver_realDevice.loadAppiumDriver()

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_atp_esky(self):
        "Testing the Esky app "
        self.driver.implicitly_wait(30)
        time.sleep(5)

        homePage = Home_Page(self.driver)
        airports_shearch_Page = Airports_search(self.driver)
        
        homePage.DEPARTUE_INPUT().click()

        airports_shearch_Page.NAME_CITY_FROM().send_keys('Kat')
        time.sleep(5)

        print(homePage.Results_cities()[0].find_element_by_id('com.homePage:id/tv_airport_list_suggestion').text+ ' obiekt 0')
        print(homePage.Results_cities()[1].find_element_by_id('com.homePage:id/tv_airport_list_suggestion').text+ ' obiekt 1')
        print(homePage.Results_cities()[2].find_element_by_id('com.homePage:id/tv_airport_list_suggestion').text+ ' obiekt 2')
        print(homePage.Results_cities()[3].find_element_by_id('com.homePage:id/tv_airport_list_suggestion').text+ ' obiekt 3')
        print(homePage.Results_cities()[4].find_element_by_id('com.homePage:id/tv_airport_list_suggestion').text+ ' obiekt 4')
        #print(homePage.Results_cities()[5].find_element_by_id('com.homePage:id/tv_airport_list_suggestion').text+ 'obiekt 5')
        #print(homePage.Results_cities()[6].find_element_by_id('com.homePage:id/tv_airport_list_suggestion').text+ 'obiekt 6')


        homePage.Results_cities()[0].click()
        time.sleep(1)
        #to destination input
        homePage.DESTIN_INPUT().click()
        homePage.Name_CITY_TO().send_keys('Warszawa')
        print(homePage.Results_cities()[0].find_element_by_id('com.homePage:id/tv_airport_list_suggestion').text+ ' obiekt 0')

        homePage.Results_cities()[0].click()

        homePage.SEARCH_BUTTON().click()
        time.sleep(5)
       # print(str(self.driver.page_source))

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_esky_app)
    unittest.TextTestRunner(verbosity=2).run(suite)
