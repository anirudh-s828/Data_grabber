# To get more cooler libraries that can help you do python easily                                                              #
# open your browser and type in this link https://discord.gg/F9wQ5yNB and join my server's python channel if you have a discord#
# open your instagram and follow me, my username is                                                                            #
################################################################################################################################
import datetime
    
import socket

from pip._internal import main as pipmain

try:
    import psutil
except:
    pipmain(['install','psutil'])
    import psutil


try:
    import wikipedia
except:
    pipmain(['install', 'wikipedia'])
    import wikipedia

try:
    import imdb
except:
    pipmain(['install','IMDbPY'])
    import imdb
try:
    import requests
except:
    pipmain(['install','requests'])
    import requests

import bs4

try:
    import cv2
except:
    pipmain(['install','opencv-python'])

try:
    import platform
except:
    pipmain(['install'],['platform'])

try:
    from PyDictionary import PyDictionary
except:
    pipmain(['install','PyDictionary'])
    from PyDictionary import PyDictionary

class data_grabber:
    def grab_wikipedia(self,search, lines):
        result = wikipedia.summary(search, sentences = lines) 
        return result
    def grab_GoogleResult(self, search):
        url = "https://www.google.com/search?q=" + search
        request_result = requests.get( url )
  
        # Pulling HTTP data from internet 
        soup = bs4.BeautifulSoup( request_result.text 
                                , "html.parser" )
        
        # Finding temperature in Celsius.
        # The temperature is stored inside the class "BNeawe". 
        temp = soup.find( "div" , class_='BNeawe' ).text 
        return temp
    def grab_Meaning(self, word):
        dict = PyDictionary()
  
        meaning = dict.meaning(word)
        return meaning
    def grab_dateTime(self,requirements):
        '''
        the argument requirements must be a string 
        key words : %Y for year, %m for month, %d for day, %H for hours, %M for minutes and %S for seconds
        '''
        e = datetime.datetime.now()
        try:
            return e.strftime(requirements)
        except:
            raise Exception("the argument requirements must be a string. key words : %Y for year, %m for month, %d for day, %H for hours, %M for minutes and %S for seconds")
    def grab_pcBattery(self):
        battery = psutil.sensors_battery()
        return battery.percent
    def grab_pcInfo(self):
        my_system = platform.uname()
        return [my_system.system,my_system.node,my_system.release,my_system.version,my_system.machine,my_system.processor]
    def grab_ipAdress(self):
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    def grab_MyLocation(self):
        responce = requests.get('https://ipinfo.io/json').json()
        return responce
    def grab_File(self,filename):
        try:
            x = open(filename, mode = 'r')
            y = x.read()
            x.close()
            return y
        except:
            raise Exception('error')
    def grab_HostName(self):
        return socket.gethostname()
