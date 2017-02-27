import os
import unittest
from time import sleep

from appium import webdriver


class ApiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
     #   desired_caps['platformVersion'] = '6.0 Marshmallow (API Level 23'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'

        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apk/shopping.list.grocery.recipes.coupons.apk'))
        desired_caps['appPackage'] = 'shopping.list.grocery.recipes.coupons'
        desired_caps['appActivity'] = 'android.intent.category.LAUNCHER' # incorect propably
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        sleep(2)
        # example from https://qxf2.com/blog/appium-mobile-automation/
        # element = self.driver.find_element_by_name("PLAY!")
        # element.click()
        # self.driver.find_element_by_name("Single Player").click()
        # textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        # self.assertEqual('MATCH SETTINGS', textfields[0].text)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ApiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

