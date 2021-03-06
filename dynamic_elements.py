import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver=self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver

        option=[]
        menu=5
        tries=1

        while len(option) < 5:
            option.clear()

            for i in range(menu):
                try:
                    option_name=driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i+1}]/a')
                    option.append(option_name.text)
                    print(option)
                except:
                    print(f'Option number {i+1} is not found')
                    tries +=1
                    driver.refresh()

        print(f'Finished in {tries} tries')            

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main(verbosity=2)
