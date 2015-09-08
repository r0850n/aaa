from selenium.webdriver.common.by import By
from common.pageobject_support import cacheable, callable_find_by as find_by, callable_find_by

from time import sleep
import time






class Home_Page(object):
    
    MENU_BUTTON = find_by(how=By.CLASS_NAME, using='android.widget.ImageButton')
    SEARCH_BUTTON = find_by(how=By.CLASS_NAME,using='android.widget.Button')
    DEPARTUE_INPUT = find_by(how=By.ID, using='com.esky:id/qsf_departure_input')
    DESTIN_INPUT = find_by(how=By.ID, using='com.esky:id/qsf_arrival_input')
    TAB_ROUNDTRIP = find_by(how=By.ID, using='com.esky:id/qsf_tab_roundtrip')
    TAB_ONEWAY = find_by(how=By.ID, using='com.esky:id/qsf_tab_oneway')
    DATE_DEPARTUE_INPUT = find_by(how=By.ID, using='com.esky:id/qsf_date_departure_input') 
    DATE_ARRIVAL_INPUT = find_by(how=By.ID, using='com.esky:id/qsf_date_arrival_input')
    PASSENGER_INPUT = find_by(how=By.ID, using='com.esky:id/qsf_passenger_input')
    
    
    def __init__(self,driver):
        self._driver = driver
        
class Airports_search(object):
    
    NAME_CITY_FROM = find_by(how=By.ID, using='com.esky:id/autocomplete_search_input')
    Results_cities = callable_find_by(how=By.XPATH, using='//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout'
                                      ,multiple=True)
    
    
   
        
    def __init__(self,driver):
        self._driver = driver

class CallendarPage(object):
    
    Next_Month = find_by(how=By.ID, using='com.esky:id/next_month')
    DAY = callable_find_by(how=By.XPATH, using='//android.widget.GridView/android.widget.RelativeLayout', multiple=True)
    
    
        
    
    def __init__(self,driver):
        self._driver = driver      
        
        
class Global_Methods(object):

      
    DESTIN_INPUT = find_by(how=By.ID, using='com.esky:id/qsf_arrival_input')
    # to another template imput from:
    
    Name_CITY_TO = find_by(how=By.ID, using='com.esky:id/autocomplete_search_input')

    Results_cities = callable_find_by(how=By.XPATH, using='//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout'
                                      ,multiple=True)
    
    

    def setDepartuedDate(self, hp):
        
        hp.DATE_DEPARTUE_INPUT().click()
        
    def findelement(self,text):
        element = find_by(how=By.XPATH, using='//text[@text='+text+']')
        elem= self._driver.find_element_by_xpath('//android.widget.TextView[@text='+text+']')
        return elem   

    def travel_from_to(self, departue, arrival,date1,date2):
        
        hp=Home_Page(self._driver)
        ap=Airports_search(self._driver)
        es=Global_Methods(self._driver)
        
        #hp.DEPARTUE_INPUT().click()
       # ap.NAME_CITY_FROM().send_keys(departue)
       # ap.Results_cities()[0].click()
       # time.sleep(5)
        self.setLocation(departue)
        hp.DESTIN_INPUT().click()
        ap.NAME_CITY_FROM().send_keys(arrival)
        ap.Results_cities()[0].click()
        time.sleep(5)
        hp.DATE_DEPARTUE_INPUT().click()
        self.findelement(date1).click()
        hp.DATE_ARRIVAL_INPUT().click()
        self.findelement(date2).click()
        hp.SEARCH_BUTTON().click()
        time.sleep(5)
        

    def __init__(self, driver):
        self._driver = driver
       