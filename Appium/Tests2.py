import os
import unittest

from appium import webdriver


class ChessAndroidTests(unittest.TestCase):
    "Class to run tests against the Chess Free app"

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apk/Chess_Free.apk'))
        desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_caps['appActivity'] = '.ChessFreeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_single_player_mode(self):
        "Test the Single Player mode launches correctly"
        element = self.driver.find_element_by_name("PLAY!")
        element.click()
        self.driver.find_element_by_name("Single Player").click()
        textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual('MATCH SETTINGS', textfields[0].text)

        element = self.driver.find_element_by_name("PLAY")
        element.click()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
