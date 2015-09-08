from appium import webdriver
from common import settings




class LoadDriver_realDevice(object):

    @staticmethod
    def loadAppiumDriver():

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = settings.emu
        # Since the app is already installed launching it using package and activity name       
        desired_caps['app'] = r'F:\automaty\esky\com.esky.apk'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        #desired_caps['appWaitActivity'] = '.activity.root.TournamentList'
        return webdriver.Remote(settings.appiumHub2, desired_caps)


