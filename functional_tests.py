from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_sign_up_as_volunteer(self):

        # Edith is immune from Coronavirus and wants to volunteer
        # for ImmuneCorps. She goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention ImmuneCorps.
        self.assertIn('ImmuneCorps', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ImmuneCorps', header_text)

        # She sees a box to click to join ImmuneCorps. She clicks on the
        # box.
        join_button = self.browser.find_element_by_id('id_join_immunecorps')
        join_button.click()
        time.sleep(1)

        # She sees a place to enter in her email to join, enters in
        # her email
        emailinputbox = self.browser.find_element_by_id('email')
        self.assertEqual(
            emailinputbox.get_attribute('placeholder'),
            'Enter your email'
        )
        emailinputbox.send_keys('test@example.com')

        # She clicks the box to submit her information
        submit_button = self.browser.find_element_by_id('id_submit')
        submit_button.click()
        time.sleep(1)

        # The page updates and she sees a message to check
        # her email to confirm her login.
        message_text = self.browser.find_element_by_id('check_email_msg').text
        self.assertIn('Thank you for signing up for ImmuneCorps! Please check your Email', header_text)

        self.fail('Finish the test!')

        # She visits the homepage again and tries to submit her information
        # again.

        # The application does not allow her to enter in the information 
        # a second time.

        # Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
