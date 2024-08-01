from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest




class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
        #self.driver.get('https://morning-river-89959-5d7f1cb92b6d.herokuapp.com/#it-will-be-nice-to-do-a-static-site')
        self.driver.get('http://0.0.0.0:8000/')

    def test_homepage(self):   
        time.sleep(2) # Let the user actually see something!
        self.assertEqual(self.driver.title, "Gabriel Soler")
        #user arrives to the site and sees a picture of me
        element = self.driver.find_element(By.ID,'landing-text')
        self.assertEqual(element.text,'Making Therapy Creative')
        #user arrives to the site and sees a picture of me and my name in a navbar
        nav = self.driver.find_element(By.ID,'nav-title')
        self.assertEqual(nav.text,'Gabriel Soler Psychotherapist')
        time.sleep(1) # Let the user actually see something!
        #user scrolls down and finds links with areas of my work, presses creativity
        link = self.driver.find_element(By.LINK_TEXT, 'Creativity')
        self.assertEqual(link.text,'Creativity')
        link = self.driver.find_element(By.LINK_TEXT, 'Migration')
        self.assertEqual(link.text,'Migration')
        link = self.driver.find_element(By.LINK_TEXT, 'Neurodiversity')
        self.assertEqual(link.text,'Neurodiversity')
        link = self.driver.find_element(By.LINK_TEXT, 'Intelectual Depth')
        self.assertEqual(link.text,'Intelectual Depth')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()