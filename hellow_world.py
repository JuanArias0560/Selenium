import unittest 
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class hellow_world(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver=cls.driver
        driver.implicitly_wait(10)

    def test_hellow_world(self):
        driver=self.driver
        driver.get('https://www.platzi.com')

    def test_vist_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity= 2 , testRunner= HTMLTestRunner(output= 'Report' , report_name= 'Hello-word-report'))