import unittest
from selenium import webdriver
from google_page import Googlepage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.drive=webdriver.Chrome(executable_path='/usr/bin/chromedriver')

    def test_search(self):
        google=Googlepage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    @classmethod    
    def tearDownClass(cls):
        cls.drive.close()

if __name__=='__main__':
    unittest.main(verbosity=2)
        