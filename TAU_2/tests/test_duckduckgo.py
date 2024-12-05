from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestSearchEngine(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_functionality(self):
        driver = self.driver
        driver.get("https://www.duckduckgo.com")

        title = driver.title
        self.assertIn("DuckDuckGo", title, 'Tytuł nie zawiera "DuckDuckGo"')

        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys("Best programming practices in Python")
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.wLL07_0Xnd1QZpzpfR4W'))
        )

        title = driver.title
        self.assertIn("Best programming practices", title, 'Tytuł nie zawiera "Best programming practices"')

        results = driver.find_elements(By.CSS_SELECTOR, '.wLL07_0Xnd1QZpzpfR4W')
        self.assertGreater(len(results), 0, 'Brak wyników wyszukiwania')

        first_result = results[0].text
        self.assertTrue(
            "Python" in first_result or "Programming" in first_result,
            'Pierwszy wynik nie zawiera "Python" ani "Programming"'
        )

        print("Search functionality test completed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
