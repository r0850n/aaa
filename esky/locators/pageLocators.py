from selenium.webdriver.common.by import By
from common.pageobject_support import cacheable, callable_find_by as find_by, callable_find_by

from time import sleep
import time

 
  #chose your language
class Welcome_Page(object):
    #Polski
    PL = find_by(how=By.ID, using='com.esky:id/lang_chooser_PL')
    BG = find_by(how=By.ID, using='com.esky:id/lang_chooser_BG')
     #ro
    RO = find_by(how=By.ID, using='com.esky:id/lang_chooser_RO')
     
    def __init__(self,driver):
        self._driver = driver
       
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
  
class Menu(object):
     
    FLIGHTS = find_by(how=By.ID, using='com.esky:id/drawer_item_flights')
    CARS = find_by(how=By.ID, using='com.esky:id/drawer_item_cars')
    APPLICATION_RATE = find_by(how=By.ID, using='com.esky:id/drawer_item_rate_app')
    SETTINGS = find_by(how=By.ID, using='com.esky:id/drawer_item_settings')
    INFO = find_by(how=By.ID, using='com.esky:id/drawer_item_info')
     
    def goto_Flights(self):
        self.FLIGHTS().click()
         
    def goto_Cars(self):
        self.CARS().click()
     
    def __init__(self,driver):
        self._driver = driver     
         
class Airports_search(object):
     
    NAME_CITY_FROM = find_by(how=By.ID, using='com.esky:id/autocomplete_search_input')
    Results_cities = callable_find_by(how=By.XPATH, using='//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout'
                                      ,multiple=True)
    Result_travel = callable_find_by(how=By.XPATH, using="//android.widget.ExpandableListView/android.widget.RelativeLayout", multiple=True)
    Result_child_container = callable_find_by(how=By.ID, using='com.esky:id/sf_list_child_container', multiple=True)
    Select_button = find_by(how=By.ID, using='com.esky:id/flight_details_select')
     
    def select_travel_where(self,time_arival=None):
         
        if(time_arival== None):
            self.Result_travel()[0].click()
            self.Result_child_container()[0].click()
            time.sleep(10)
            self.Select_button().click()
             
#             print(self._driver.page_source())
        else:
            self.Result_travel()[0].click()
            for element in self.Result_child_container():
                hour = element.find_element_by_id("com.esky:id/sf_list_child_header_hours")
                if hour.get_attribute("text") ==time_arival:
                    element.click()
    
         
    def __init__(self,driver):
        self._driver = driver
 
class CallendarPage(object):
     
    Next_Month = find_by(how=By.ID, using='com.esky:id/next_month')
    DAY = callable_find_by(how=By.XPATH, using='//android.widget.GridView/android.widget.RelativeLayout', multiple=True)
    Current_month = find_by(how=By.ID, using='com.esky:id/current_month')
     
         
    def setDate(self, m, day):
        Home_Page.DATE_DEPARTUE_INPUT().click()
        while self.Current_month().get_attribute("text") != m:
            self.Next_Month().click()
        self.findelement(day).click()
             
         
    def __init__(self,driver):
        self._driver = driver      
        #Loader.__init__(self, driver)
         
class Book_a_flight(object):
     
     
    def __init__(self,driver):
        self._driver = driver      
       
 
         
class Global_Methods(object):
 
     
    def setDepartuedDate(self,day):
         
        Home_Page.DATE_DEPARTUE_INPUT().click()
        self.findelement(day).click()
         
    def setArrivalDate(self,day):
         
        Home_Page.DATE_ARRIVAL_INPUT().click()
        self.findelement(day).click()    
         
    def findelement(self,text):
         
        elem= self._driver.find_element_by_xpath('//android.widget.TextView[@text='+text+']')
        return elem   
 
 
    def rountrip(self, departue, arrival, m, date1, date2):
        #set location from:
        self.setLocationFrom(departue)
        #setLocation to:
        self.setLocationTo(arrival)
        #set departue Date:
        #self.setDepartuedDate(date1)
        CallendarPage.setDate(m, date1)
        #set arrival date:
        self.setArrivalDate(date2)
        Home_Page.SEARCH_BUTTON().click()
        #time.sleep(2)
        #select travel
        Airports_search.select_travel_where()
         
         
    def oneway(self, departue, arrival, m, date1):
        #go to onewayT ab
        Home_Page().TAB_ONEWAY().click()
        #set location from:
        self.setLocationFrom(departue)
        #setLocation to:
        self.setLocationTo(arrival)
        #set departue Date:
        #self.setDepartuedDate(date1)
        CallendarPage.setDate(m, date1)
         
        self.get_HomePage().SEARCH_BUTTON().click()
         
        #select travel
        Airports_search.select_travel_where()
 
    def travel_from_to(self,roundtrip, departue, arrival,m, date1,date2):
        if roundtrip:
            self.rountrip(departue, arrival, m, date1, date2)
        else:
            self.oneway(departue, arrival, m, date1)
 
    def __init__(self, driver):
        self._driver = driver
        #Loader.__init__(self, driver)
         
         
                