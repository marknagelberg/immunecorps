from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


class NewVolunteerTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_sign_up_as_volunteer(self):

        # Edith is immune from Coronavirus and wants to volunteer
        # for ImmuneCorps. She goes to check out its homepage.
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention ImmuneCorps.
        self.assertIn('ImmuneCorps', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ImmuneCorps', header_text)

        # She sees a box to click to join ImmuneCorps. She clicks on the
        # box.
        join_button = self.browser.find_element_by_id('id_join_immunecorps')
        join_button.click()

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

        # The page updates and she sees a message to check
        # her email to confirm her login.
        message_text = self.browser.find_element_by_id('check_email_msg').text
        self.assertIn('Thank you for signing up for ImmuneCorps! ', message_text)

        # She leaves

    def test_multiple_volunteers_have_different_urls(self):

        # Edith signs up to volunteer for ImmuneCorps
        self.browser.get(self.live_server_url)
        join_button = self.browser.find_element_by_id('id_join_immunecorps')
        join_button.click()
        emailinputbox = self.browser.find_element_by_id('email')
        emailinputbox.send_keys('edith@example.com')

        # She clicks the box to submit her information
        submit_button = self.browser.find_element_by_id('id_submit')
        submit_button.click()

        # She logs in
        self.browser.get(self.live_server_url)
        login_button = self.browser.find_element_by_id('id_vlogin_immunecorps')
        login_button.click()
        emailinputbox = self.browser.find_element_by_id('login_email')
        emailinputbox.send_keys('edith@example.com')
        submit_button = self.browser.find_element_by_id('id_submit')
        submit_button.click()

        # She notices the page indicating she signed up has a unique URL
        edith_volunteer_url = self.browser.current_url
        self.assertRegex(edith_volunteer_url, '/volunteers/.+')

        # Now a new user Francis comes to the site

        ## Create new browser session to ensure no info from Edith
        ## coming from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page and signs up
        self.browser.get(self.live_server_url)
        join_button = self.browser.find_element_by_id('id_join_immunecorps')
        join_button.click()
        emailinputbox = self.browser.find_element_by_id('email')
        emailinputbox.send_keys('francis@example.com')
        submit_button = self.browser.find_element_by_id('id_submit')
        submit_button.click()

        # He logs in
        self.browser.get(self.live_server_url)
        login_button = self.browser.find_element_by_id('id_vlogin_immunecorps')
        login_button.click()
        emailinputbox = self.browser.find_element_by_id('login_email')
        emailinputbox.send_keys('francis@example.com')
        submit_button = self.browser.find_element_by_id('id_submit')
        submit_button.click()
        francis_volunteer_url = self.browser.current_url
        self.assertRegex(francis_volunteer_url, '/volunteers/.+')
        self.assertNotEqual(francis_volunteer_url, edith_volunteer_url)

    def test_layout_and_styling(self):
        # Edith goes to home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        # She notices the join button that is nicely centred
        join_button = self.browser.find_element_by_id('id_join_immunecorps')
        self.assertAlmostEqual(
            join_button.location['x'] + join_button.size['width'] / 2,
            512,
            delta=10
        )
        # She clicks the join and notices the email input box is nicely centred
        join_button.click()
        emailinputbox = self.browser.find_element_by_id('email')
        self.assertAlmostEqual(
            emailinputbox.location['x'] + emailinputbox.size['width'] / 2,
            512,
            delta=10
        )


class HealthAuthorityAdminTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_reviewers(self):

        # Bob the Health Authority IT Admin guy just installed ImmuneCorps.
        # He wants to add Dr. Johnson in his organization to have access
        # to ImmuneCorps so he can add data about immune patients,
        # and verify volunteers as immune.

        self.fail('Finish the test!')
        # Bob goes to the /admin path as specified in the installation docs

        # Bob enters in his user / pass, logs in and sees he is in the Admin
        # Console

        # He sees a link to manage Health Authority users and clicks

        # He adds Dr. Johnson's information and submits it

        # He navigates back to the main admin console page. He goes back
        # to the Health Authority user page and still sees Dr. Johnson's
        # information there.


class NewHealthAuthorityStaffTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_verify_applicant_immunity(self):

        self.fail('Finish the test!')
        # Immunity Tracking Staff Claire logs into the staff portal

        # She sees two new applicants wanting to be Immune-Verified

        # She clicks on "Browse Immune Records" to check to see whether
        # they are recorded as immune.

        # She sees the first person in the list of immune and clicks
        # button to link the applicant to the immune record and mark them as 
        # immune.

        # She goes back to the page of immune applicants and sees the other
        # applicant record there. She clicks "Browse Immune Records"

        # She can't find the record for this person, so she marks them as
        # unverified.

    def test_can_add_immunity_records(self):

        self.fail('Finish the test!')
        # Immunity Tracking Staff Claire logs into the staff portal

        # She clicks a button to browse the immune inventory

        # Once there, she clicks the button to add a new immune person to the 
        # inventory

        # She enters in the person's information and clicks submit

        # She sees the record of the newly added immune person

    def test_can_add_immunity_records_via_api(self):

        self.fail('Finish the test!')
        # The Health Authority has requested that Mark, a software engineer
        # from the IT department, add existing records of the immune that
        # are currently stored in an Excel file. Luckily he can do this
        # quickly through the API

        # He logs into his staff portal

        # He clicks on the API button

        # He clicks on the button to generate an API key

        # He makes a request using the API key to add a new immune record

        # He make a request using the API to get the immune record just added

