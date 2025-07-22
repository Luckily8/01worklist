from appium.webdriver.common.appiumby import AppiumBy

class MinePage:
    def __init__(self, driver):
        self.driver = driver

    def goto_setting(self):
        try:
            self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/tvSetting").click()
        except Exception as e:
            from utils.AppiumUtils import AppiumUtils as AU
            AU.save_screenshot("goto_setting失败")
            print(f"goto_setting异常: {e}")
            raise

    def goto_logout(self):
        try:
            self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/tvLogout").click()
        except Exception as e:
            from utils.AppiumUtils import AppiumUtils as AU
            AU.save_screenshot("goto_logout失败")
            print(f"goto_logout异常: {e}")
            raise

    def confirm_alert(self):
        try:
            self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/dialog_alert_two_confirm").click()
        except Exception as e:
            from utils.AppiumUtils import AppiumUtils as AU
            AU.save_screenshot("confirm_alert失败")
            print(f"confirm_alert异常: {e}")
            raise

    def assert_mine_page(self):
        try:
            el = self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/llMine")
            assert el is not None, "断言失败：未找到我的页面元素"
            return el
        except Exception as e:
            from utils.AppiumUtils import AppiumUtils as AU
            AU.save_screenshot("assert_mine_page失败")
            print(f"assert_mine_page异常: {e}")
            raise

    def click_mine(self):
        try:
            self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/llMine").click()
        except Exception as e:
            from utils.AppiumUtils import AppiumUtils as AU
            AU.save_screenshot("click_mine失败")
            print(f"click_mine异常: {e}")
            raise
