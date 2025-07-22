from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_phone_login(self):
        self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/cvPhoneLogin").click()

    def input_phone(self, phone):
        self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/etPhone").send_keys(phone)

    def click_login_or_register(self):
        self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/tvLoginOrRegister").click()

    def click_alert_confirm(self):
        self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/dialog_alert_two_confirm").click()

    def click_code_input(self):
        self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/tvLoginOrRegister").click()

    def input_sms_code(self, code_func):
        code_func()  # 传入验证码输入方法

    def click_next(self):
        self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/tvNext").click()

    def login_flow(self, phone, code_func):
        self.click_phone_login()
        self.input_phone(phone)
        self.click_login_or_register()
        self.click_alert_confirm()
        self.click_code_input()
        self.click_next()
        code_func()
        self.click_next()

    def assert_mine_page(self):
        el = self.driver.find_element(AppiumBy.ID, "com.mix.upup:id/llMine")
        assert el is not None, "断言失败：未找到我的页面元素"
        el.click()
        return el
