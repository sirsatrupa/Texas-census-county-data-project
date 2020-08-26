# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:53:29 2020

@author: tsbloxsom
"""

from pyvirtualdisplay import Display
from selenium import webdriver

with Display():
    # we can now start Firefox and it will run inside the virtual display
    browser = webdriver.Firefox()
    # put the rest of our selenium code in a try/finally
    # to make sure we always clean up at the end
    try:
        browser.get('https://www.google.ca/')
        print(browser.title) #this should print "Google"
        finally:
            browser.quit()
