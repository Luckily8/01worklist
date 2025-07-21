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
wait = WebDriverWait(driver, 20)

copilot_name = "     "  # 替换为实际测试副驾驶姓名
nick_name = "     "  # 替换为实际测试副驾驶昵称

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

# 返回主页
while True:
	driver.back()
	try:
		el = WebDriverWait(driver, 0.5).until(
			EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Toast[@text='再按一次退出']"))
		)
		if "再按一次退出" in el.text:
			break
	except Exception:
		pass



el12 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/llMine", log_msg="点击我的")
el12.click()
el13 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/tvSetting", log_msg="点击设置")
el13.click()
el14 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/tvCopilotSetting", log_msg="点击副驾驶设置")
el14.click()
el15 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/ll_name", log_msg="点击姓名")
el15.click()
el16 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/name_edit", log_msg="输入姓名")
el16.clear()
el16.send_keys(copilot_name)  # 替换为实际测试姓名
el17 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/title_edit", log_msg="输入昵称")
el17.clear()
el17.send_keys(nick_name)  # 替换为实际测试昵称
el18 = wait_and_log(AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(0)", log_msg="点击确认")
el18.click()
el19 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/dialog_alert_two_confirm", log_msg="点击确认")
el19.click()
el12 = wait_and_log(AppiumBy.CLASS_NAME, value="android.widget.ImageView", log_msg="点击返回")
el12.click()
el13 = wait_and_log(AppiumBy.ID, value="com.mix.upup:id/tvCopilot", log_msg="点击副驾驶")
el13.click()

print(">>>>>>>>> 已完成copilot设置流程")
