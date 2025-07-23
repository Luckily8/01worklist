from appium.webdriver.common.appiumby import AppiumBy
from utils.exception_handler import handle_exceptions
from utils.AppiumUtils import AppiumUtils as AU
class MinePage:
    def __init__(self, driver):
        self.driver = driver

    @handle_exceptions
    def goto_setting(self):
        AU.wait_and_log_then_click("com.mix.upup:id/tvSetting")

    @handle_exceptions
    def goto_logout(self):
        AU.wait_and_log_then_click("com.mix.upup:id/tvLogout")

    @handle_exceptions
    def confirm_alert(self):
        AU.wait_and_log_then_click("com.mix.upup:id/dialog_alert_two_confirm")

    @handle_exceptions
    def assert_mine_page(self):
        el = AU.wait_and_log("com.mix.upup:id/llMine")
        assert el is not None, "断言失败：未找到我的页面元素"
        return el

    @handle_exceptions
    def click_mine(self):
        AU.wait_and_log_then_click("com.mix.upup:id/llMine")
