from utils.request_handler import RequestHandler
from utils.yaml_handler import load_yaml

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


# 导入配置文件和测试数据
config = load_yaml("config/config.yaml")
# 设置Appium选项
options = AppiumOptions()
options.load_capabilities(config)
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
# 初始化请求处理器
class AppiumUtils:
	driver = driver  # 设置为类属性，供全局调用
	@staticmethod
	def wait_and_log_then_click(value, by=AppiumBy.ID, timeout=15, log_msg=None):
		global driver
		try:
			element = WebDriverWait(driver, timeout if timeout else 8).until(
				EC.presence_of_element_located((by, value))
			)
			element.click()
		except Exception as e:
			print(f"元素未出现: {log_msg if log_msg else value}, 错误: {e}")
			raise

	@staticmethod
	def wait_and_log(value, by=AppiumBy.ID, timeout=15, log_msg=None):
		global driver
		try:
			element = WebDriverWait(driver, timeout if timeout else 8).until(
				EC.presence_of_element_located((by, value))
			)
			return element
		except Exception as e:
			print(f"元素未出现: {log_msg if log_msg else value}, 错误: {e}")
			raise	

	@staticmethod
	def return_to_home():
		global driver
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

	@staticmethod
	def sms_code_input():	
		for _ in range(4):
			# 模拟手动输入验证码 9999
			actions = ActionChains(driver)
			actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
			actions.w3c_actions.pointer_action.move_to_location(845, 2242)
			actions.w3c_actions.pointer_action.pointer_down()
			actions.w3c_actions.pointer_action.pause(0.09)  # 缩短模拟点击间隔
			actions.w3c_actions.pointer_action.release()
			actions.perform()
			
	@staticmethod
	def drag_copilot_and_quit_youth():
		global driver
		# 如果检测到青少年模式提示，则拖动 copilot 浮窗并退出提示
		try:
			AppiumUtils.wait_and_log_then_click(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("青少年模式")', log_msg="青少年模式图片")
		except Exception:
			print("未检测到青少年模式提示，跳过")
			return # 如果没有检测到提示，则直接返回
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
		el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='com.mix.upup:id/imgBack']/android.view.View")
		el1.click()
		print("退出青少年模式提示")
	
	@staticmethod
	def save_screenshot(filename=None):
		global driver
		import time, os
		now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
		if filename is None:
			filename = f"screenshot_{now}"
		else:
			filename = f"{filename.replace(' ', '_')}_{now}"
		save_dir = "screenshot"
		if not os.path.exists(save_dir):
			os.makedirs(save_dir)
		save_path = os.path.join(save_dir, filename + ".png")
		result = driver.get_screenshot_as_file(save_path)
		print(f"截图已保存到: {save_path}, 成功: {result}")
		return save_path