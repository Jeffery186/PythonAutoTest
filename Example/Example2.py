# Selenium WebDriver is often used as a basis for testing web applications. Here is a simple example using Python’s
# standard unittest library: http://docs.python.org/3/library/unittest.html

import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google',self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)