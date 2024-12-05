from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_functionality(self):
        driver = self.driver
        driver.get("https://www.google.com")

        try:
            accept_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, 'L2AGLb'))
            )
            accept_button.click()
        except:
            pass

        self.assertIn("Google", driver.title)

        search_input = driver.find_element(By.NAME, 'q')
        search_input.send_keys("Python automation testing")
        search_input.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.title_contains("Python automation testing")
        )

        self.assertIn("Python automation testing", driver.title)

        search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
        self.assertGreater(len(search_results), 0)

        self.assertIn("Python", driver.current_url)

        print("Search test completed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
