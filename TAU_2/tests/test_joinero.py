from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestEcommerce(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_and_add_to_cart(self):
        driver = self.driver
        driver.get("https://joinero.pl")

        title = driver.title
        self.assertIn("Joinero", title)

        search_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Szukaj produktów..."]')
        search_input.send_keys('b')

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="absolute"] a'))
        )

        suggestions = driver.find_elements(By.CSS_SELECTOR, 'div[class*="absolute"] a')
        suggestions[0].click()

        WebDriverWait(driver, 10).until(EC.title_contains('Poznajmy się'))

        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Dodaj do koszyka')]"))
        )
        add_to_cart_button.click()

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'a[href="/koszyk"] div span'), '1'
            )
        )

        print("E-commerce functionality test completed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
