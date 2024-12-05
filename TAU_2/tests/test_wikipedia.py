from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestKnowledgeSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_article_navigation(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")

        title = driver.title
        self.assertIn("Wikipedia", title)

        search_input = driver.find_element(By.NAME, 'search')
        search_input.send_keys("Python programming", Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'firstHeading'))
        )

        article_title = driver.find_element(By.ID, 'firstHeading').text
        self.assertIn("Python", article_title)

        article_body = driver.find_element(By.ID, 'bodyContent').text
        self.assertIn("language", article_body)

        first_link = driver.find_element(By.CSS_SELECTOR, '#bodyContent a')
        first_link_text = first_link.text
        first_link.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'firstHeading'))
        )

        new_article_title = driver.find_element(By.ID, 'firstHeading').text
        self.assertIn(first_link_text, new_article_title)

        new_article_body = driver.find_element(By.ID, 'bodyContent').text
        self.assertIn("syntax", new_article_body)

        print("Knowledge site navigation test completed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
