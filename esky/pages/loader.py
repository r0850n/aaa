
import time
from selenium.webdriver.common.by import By
from common.pageobject_support import cacheable, callable_find_by as find_by, callable_find_by
from calendar import month



class Loader(object):

    def __init__(self, driver):
        self.driver = driver

    def get_HomePage(self):
        return Home_Page(self.driver)
    
    def get_Welcome_Page(self):
        return Welcome_Page(self.driver)

    def get_Airports_Page(self):
        return Airports_search(self.driver)
    
    def get_Global_Methods(self):
        return Global_Methods(self.driver)
    
    def get_Callendar_Page(self):
        return CallendarPage(self.driver)

    def getText(self, obj):
        return obj.get_attribute('text')

    def findelement(self,text):
        elem= self._driver.find_element_by_xpath('//android.widget.TextView[@text='+text+']')
        return elem   
    
    def setLocationFrom(self, location):
        self.get_HomePage().DEPARTUE_INPUT().click()
        self.get_Airports_Page().NAME_CITY_FROM().send_keys(location)
        self.get_Airports_Page().Results_cities()[0].click()
        #time.sleep(2)
     
    def setLocationTo(self,location): 
        self.get_HomePage().DESTIN_INPUT().click()
        self.get_Airports_Page().NAME_CITY_FROM().send_keys(location)
        self.get_Airports_Page().Results_cities()[0].click()
        #time.sleep(2)
          
  
  #chose your language
class Welcome_Page(object):
    #Polski
    PL = find_by(how=By.ID, using='com.esky:id/lang_chooser_PL')
    BG = find_by(how=By.ID, using='com.esky:id/lang_chooser_BG')
     #ro
    RO = find_by(how=By.ID, using='com.esky:id/lang_chooser_RO')
      
class Home_Page(Loader):
    
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

class CallendarPage(Loader):
    
    Next_Month = find_by(how=By.ID, using='com.esky:id/next_month')
    DAY = callable_find_by(how=By.XPATH, using='//android.widget.GridView/android.widget.RelativeLayout', multiple=True)
    Current_month = find_by(how=By.ID, using='com.esky:id/current_month')
    
        
    def setDate(self, m, day):
        self.get_HomePage().DATE_DEPARTUE_INPUT().click()
        while self.Current_month().get_attribute("text") != m:
            self.Next_Month().click()
        self.findelement(day).click()
            
        
    def __init__(self,driver):
        self._driver = driver      
        Loader.__init__(self, driver)
        
class Global_Methods(Loader):

    
    def setDepartuedDate(self,day):
        
        self.get_HomePage().DATE_DEPARTUE_INPUT().click()
        self.findelement(day).click()
        
    def setArrivalDate(self,day):
        
        self.get_HomePage().DATE_ARRIVAL_INPUT().click()
        self.findelement(day).click()    
        
    def findelement(self,text):
        
        elem= self._driver.find_element_by_xpath('//android.widget.TextView[@text='+text+']')
        return elem   

    def travel_from_to(self, departue, arrival,m, date1,date2):
        
        #set location from:
        self.setLocationFrom(departue)
        #setLocation to:
        self.setLocationTo(arrival)
        
        #set departue Date:
        #self.setDepartuedDate(date1)
        self.get_Callendar_Page().setDate(m, date1)
        
        #set arrival date:
        self.setArrivalDate(date2)
        
        self.get_HomePage().SEARCH_BUTTON().click()
        #time.sleep(2)
    

    def __init__(self, driver):
        self._driver = driver
        Loader.__init__(self, driver)
        
        
        