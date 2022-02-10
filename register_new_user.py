import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()       
        driver.get('http://demo-store.seleniumacademy.com')

    def test_new_user(self):
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_botton= driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_botton.is_displayed() and create_account_botton.is_enabled())
        create_account_botton.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name=driver.find_element_by_id('firstname')
        middle_name=driver.find_element_by_id('middlename')
        last_name=driver.find_element_by_id('lastname')
        email_address=driver.find_element_by_id('email_address')
        news_letter_subscription=driver.find_element_by_id('is_subscribed')
        password =driver.find_element_by_id('password')
        confirm_password=driver.find_element_by_id('confirmation')
        submit_button=driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled() 
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled()
        )

        first_name.send_keys('afh')
        last_name.send_keys('epr')
        email_address.send_keys('shiumxluribfkxkdytnvhrw.com')
        password.send_keys('1234')
        confirm_password.send_keys('1234')
        self.driver.implicitly_wait(300)
        news_letter_subscription.click()
        submit_button.click()
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__== '__main__':
    unittest.main(verbosity= 2 , testRunner= HTMLTestRunner(output= 'Report' , report_name= 'Hello-word-report'))
    