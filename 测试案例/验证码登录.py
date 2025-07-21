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

user_phone = "17718846133"  # 替换为实际测试手机号 19812056630\13726927258（陪玩）\17718846133

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",  # 指定自动化测试的平台为 Android
    "appium:platformVersion": "15",  # 设备的 Android 系统版本号为 15
    "appium:deviceName": "AN5H6R4305000757",  # 设备名称或唯一标识符
    "appium:appPackage": "com.mix.upup",  # 要启动的应用的包名
    "appium:appActivity": "com.mix.upup.start.StartActivity",  # 应用启动时的主 Activity
    "appium:automationName": "UiAutomator2",  # 使用的自动化引擎，推荐 UiAutomator2
    "appium:ensureWebviewsHavePages": True,  # 确保 WebView 组件有页面加载（用于混合应用测试）
    "appium:nativeWebScreenshot": True,  # 使用原生方式截图 WebView 内容
    "appium:newCommandTimeout": 3600,  # 新命令超时时间（秒），防止会话过早关闭
    "appium:connectHardwareKeyboard": True,  # 连接硬件键盘，方便输入
    "appium:noReset": True,  # 启动时不重置应用状态（保留登录等信息）
    "appium:dontStopAppOnReset": True  # 重置时不停止应用（加快测试速度）
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

def quit_youth_mode():
    print("准备拖动copilot浮窗，尝试自动关闭提示...")
    # 等待屏幕内出现 text: 青少年模式
    el1 = wait_and_log(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("青少年模式")', log_msg="青少年模式图片")
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(66, 228)
    print("手指按下坐标 (66, 228)")
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(56, 896)
    print("拖动到坐标 (56, 896)")
    actions.w3c_actions.pointer_action.release()
    print("释放手指，完成拖动操作")
    actions.perform()
    print("copilot浮窗拖动操作已执行。若未生效，请尝试手动操作。")
    try:
        el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='com.mix.upup:id/imgBack']/android.view.View")
        el1.click()
        print("退出青少年模式提示")
    except Exception:
        print("未检测到青少年模式提示，跳过")

el1 = wait_and_log(AppiumBy.ID, "com.mix.upup:id/cvPhoneLogin", log_msg="手机号登录按钮")
el1.click()
el2 = wait_and_log(AppiumBy.ID, "com.mix.upup:id/etPhone", log_msg="手机号输入框")
el2.send_keys(user_phone)
el3 = wait_and_log(AppiumBy.ID, "com.mix.upup:id/tvLoginOrRegister", log_msg="登录/注册按钮")
el3.click()
el4 = wait_and_log(AppiumBy.ID, "com.mix.upup:id/dialog_alert_two_confirm", log_msg="弹窗确认按钮")
el4.click()
el5 = wait_and_log(AppiumBy.ID, "com.mix.upup:id/tvLoginOrRegister", log_msg="验证码输入按钮")
el5.click()
for _ in range(4):
    # 模拟手动输入验证码 9999
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(845, 2242)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.05)  # 缩短模拟点击间隔
    actions.w3c_actions.pointer_action.release()
    actions.perform()

el6 = wait_and_log(AppiumBy.ID, "com.mix.upup:id/tvNext", log_msg="点击下一步按钮")
el6.click()

quit_youth_mode()
print(">>>>>>>> 已结束手机号登录流程")

driver.quit()


