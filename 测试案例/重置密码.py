from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_phone = "17718846133"  # 替换为实际测试手机号 19812056630\13726927258(陪玩)\17718846133
user_password = "01ai@12345678" # 替换为实际测试密码

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:platformVersion": "15",
	"appium:deviceName": "AN5H6R4305000757",
	"appium:appPackage": "com.mix.upup",
	"appium:appActivity": "com.mix.upup.start.StartActivity",
	"appium:automationName": "UiAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
	"appium:noReset": True,
	"appium:dontStopAppOnReset": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
def wait_and_log(by, value, timeout=15, log_msg=None):
	try:
		# 优化等待时间，默认超时缩短为8秒
		element = WebDriverWait(driver, timeout if timeout else 8).until(
			EC.presence_of_element_located((by, value))
		)
		return element
	except Exception as e:
		# 只在调试时打印错误，正式运行可注释掉
		print(f"元素未出现: {log_msg if log_msg else value}, 错误: {e}")
		raise

def input_verification_code():
	for _ in range(4):
		# 模拟手动输入验证码 9999
		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(845, 2242)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.05)  # 缩短模拟点击间隔
		actions.w3c_actions.pointer_action.release()
		actions.perform()

# 返回首页
while True:
	driver.back()
	try:
		# 等待“再按一次退出”提示出现，超时缩短为0.5秒
		el = WebDriverWait(driver, 0.5).until(
			EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Toast[@text='再按一次退出']"))
		)
		if "再按一次退出" in el.text:
			break
	except Exception:
		pass

# 重置密码
el3 = wait_and_log(AppiumBy.ID, "com.mix.upup:id/llMine", log_msg="我的页面")
el3.click()
el4 = wait_and_log(AppiumBy.ID, "com.mix.upup:id/tvSetting", log_msg="设置页面")
el4.click()
el5 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/tvSecurity", log_msg="账号安全页面")
el5.click()
el4 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/tvPassword", log_msg="密码页面")
el4.click()
el5 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/etPhone", log_msg="手机号输入框")
el5.send_keys(user_phone)
el6 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/mcvNext", log_msg="下一步按钮")
el6.click()
for _ in range(4):
	# 模拟手动输入验证码 9999
	actions = ActionChains(driver)
	actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
	actions.w3c_actions.pointer_action.move_to_location(845, 2242)
	actions.w3c_actions.pointer_action.pointer_down()
	actions.w3c_actions.pointer_action.pause(0.05)  # 缩短模拟点击间隔
	actions.w3c_actions.pointer_action.release()
	actions.perform()

el12 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/tvNext", log_msg="点击下一步按钮")
el12.click()

el7 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/etNewPassword", log_msg="新密码输入框")
el7.send_keys(user_password)
el8 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/etPasswordAgain", log_msg="确认密码输入框")
el8.send_keys(user_password)
el9 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/mcvNext", log_msg="下一步按钮")
el9.click()
print(">>>>>>>> 已结束重置密码流程，开始密码登录流程")

# 密码登录流程
el1 = wait_and_log(by=AppiumBy.ID, value="com.mix.upup:id/cvPwdLogin", log_msg="密码登录按钮")
el1.click()
el2 = wait_and_log(by=AppiumBy.ID, value="com.mix.upup:id/etPhone", log_msg="手机号输入框")
el2.send_keys(user_phone)
el3 = wait_and_log(by=AppiumBy.ID, value="com.mix.upup:id/etPassword", log_msg="密码输入框")
el3.send_keys(user_password)
el4 = wait_and_log(by=AppiumBy.ID, value="com.mix.upup:id/tvLoginOrRegister", log_msg="登录/注册按钮")
el4.click()
el5 = wait_and_log(by=AppiumBy.ID, value="com.mix.upup:id/dialog_alert_two_confirm", log_msg="弹窗确认按钮")
el5.click()
el6 = wait_and_log(by=AppiumBy.ID, value="com.mix.upup:id/tvLoginOrRegister", log_msg="登录/注册按钮")
el6.click()
print(">>>>>>>> 已结束密码登录流程")
