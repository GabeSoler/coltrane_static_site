from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.test.testcases import LiveServerTestCase
import time
import unittest




class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
        #self.driver.get('https://morning-river-89959-5d7f1cb92b6d.herokuapp.com/#it-will-be-nice-to-do-a-static-site')
        self.driver.get('http://0.0.0.0:8000/')

    def test_title(self):    
        time.sleep(5) # Let the user actually see something!
        self.assertEqual(self.driver.title, "Gabriel Soler")
        #user arrives to the site and sees a picture of me
        element = self.driver.find_element(By.ID,'headshot')
        self.assertEqual(element.id,'headshot')
        #user arrives to the site and sees a picture of me
        element = self.driver.find_element(By.ID,'navbar')
        self.assertEqual(element.text,'Soler Therapy')
        time.sleep(5) # Let the user actually see something!

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()