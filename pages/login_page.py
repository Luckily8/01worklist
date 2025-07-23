
from appium.webdriver.common.appiumby import AppiumBy
from utils.exception_handler import handle_exceptions
from utils.AppiumUtils import AppiumUtils as AU
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @handle_exceptions
    def click_phone_login(self): 
        AU.wait_and_log_then_click("com.mix.upup:id/cvPhoneLogin")

    @handle_exceptions
    def input_phone(self, phone):
        el = AU.wait_and_log("com.mix.upup:id/etPhone")
        el.send_keys(phone)

    @handle_exceptions
    def click_login_or_register(self):
        AU.wait_and_log_then_click("com.mix.upup:id/tvLoginOrRegister")

    @handle_exceptions
    def click_alert_confirm(self):
        AU.wait_and_log_then_click("com.mix.upup:id/dialog_alert_two_confirm")

    @handle_exceptions
    def input_sms_code(self, code_func):
        code_func()  # 传入验证码输入方法

    @handle_exceptions
    def click_next(self):
        AU.wait_and_log_then_click("com.mix.upup:id/tvNext")

    @handle_exceptions
    def login_flow(self, phone, code_func):
        self.click_phone_login()
        self.input_phone(phone)
        self.click_login_or_register()
        self.click_alert_confirm()
        self.click_login_or_register()
        code_func()

    @handle_exceptions
    def assert_mine_page(self):
        el = AU.wait_and_log("com.mix.upup:id/llMine")
        assert el is not None, "断言失败：未找到我的页面元素"
        el.click()
        return el
