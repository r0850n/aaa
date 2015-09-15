from appium import webdriver
from common import settings

import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoadDriver_realDevice(object):
    
    

    @staticmethod
    def loadAppiumDriver():
               
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = settings.s_3
        # Since the app is already installed launching it using package and activity name       
        desired_caps['app'] =r'D:\appiumn\com.esky.apk'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        #desired_caps['appWaitActivity'] = '.activity.root.TournamentList'
        return webdriver.Remote(settings.appiumHub, desired_caps)

    @staticmethod   
    def get_desired_capabilities(app):
        
        desired_caps = {
        'platformName': 'Android',
        'platformVersion': '4.3',
        'deviceName': settings.s_3,
        'app': PATH(r'../../esky/app/' + app),
        'newCommandTimeout': 240
        }

        return desired_caps