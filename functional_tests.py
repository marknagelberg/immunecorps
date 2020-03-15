from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_deck_and_retrieve_it_later(self):

        # Edith has heard about a new flashcard management
        # tool. She goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention flashcards.
        self.assertIn('Flashcard', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Flashcard', header_text)

        # She sees boxes to to add a new flashcard Q and A. She clicks on the
        # question box.
        qinputbox = self.browser.find_element_by_id('id_new_q')
        self.assertEqual(
            qinputbox.get_attribute('placeholder'),
            'Enter a question'
        )

        # She types in "What is the capital of Manitoba?" in the question text
        # box
        qinputbox.send_keys('What is the capital of Manitoba?')

        # She clicks on the answer box
        ainputbox = self.browser.find_element_by_id('id_new_a')
        self.assertEqual(
            ainputbox.get_attribute('placeholder'),
            'Enter an answer'
        )

        # She types in "Winnipeg" in the answer text box.
        ainputbox.send_keys('Winnipeg')

        # She clicks a button to add the flashcard she entered. The page updates and
        # lists the flashcard she entered.
        submit_flashcard_button = self.browser.find_element_by_id('id_add_flashcard_button')
        submit_flashcard_button.click()
        time.sleep(1)

        table = self.browser.find_element_by_id('id_deck_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'What is the capital of Manitoba?' for row in rows),
            'New question in flashcard did not appear in table'
        )
        self.assertTrue(
            any(row.text == 'Winnipeg' for row in rows),
            'New answer in flashcard did not appear in table'
        )

        # There is still a text box inviting her to add another item. She enters in
        # "What is the capital of Canada" into the question and "Ottawa" into the answer
        # box.
        self.fail('Finish the test!')

        # She clicks a button to add the flashcard she entered. The page updates and
        # lists the flashcard she entered along with the first one.

        # Edith wonders whether the site will remember her flashcards. She
        # sees the site generated a unique URL for her.

        # She visits the URl - her to-do list is still there.

        # Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')

