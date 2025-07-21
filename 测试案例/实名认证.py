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

# 待测试身份证+姓名
id_name_list = [
    ("黄壮新", "440804200401031633"),  # 只测试格式是否允许
    ("史昕彤", "13030220030616162x"),
    ("朱有君", "652322200010200510"),
    # ...
]

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 20)

def wait_and_log(find_func, action_desc, *args, **kwargs):
    el = wait.until(lambda d: find_func(d, *args, **kwargs))
    print(f"找到元素并准备执行: {action_desc}")
    return el

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
      
el13 = wait_and_log(lambda d: d.find_element(by=AppiumBy.ID, value="com.mix.upup:id/llMine"), "点击我的")
el13.click()
el14 = wait_and_log(lambda d: d.find_element(by=AppiumBy.ID, value="com.mix.upup:id/tvAuth"), "点击实名认证")
el14.click()
el15 = wait_and_log(lambda d: d.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.LinearLayout\").instance(2)"), "点击实名类型")
el15.click()
el16 = wait_and_log(lambda d: d.find_element(by=AppiumBy.ID, value="com.mix.upup:id/et_name"), "输入姓名")

for name, id_number in id_name_list:
    el16.clear()
    el16.send_keys(name)
    print(f"已输入姓名: {name}")
    el17 = wait_and_log(lambda d: d.find_element(by=AppiumBy.ID, value="com.mix.upup:id/et_id"), "输入身份证号")
    el17.clear()
    el17.send_keys(id_number)
    print(f"已输入身份证号: {id_number}")
    driver.execute_script('mobile: hideKeyboard')
    el18 = wait_and_log(lambda d: d.find_element(by=AppiumBy.ID, value="com.mix.upup:id/mcvConfirm"), "点击确认认证")
    el18.click()
   
    # 检查是否有错误提示
    try:
        error_el = WebDriverWait(driver, 3).until(
            lambda d: d.find_element(by=AppiumBy.XPATH, value="//android.widget.Toast[@text='请输入正确的身份证号']")
        )
        print(f"姓名: {name}, 身份证号: {id_number} 不符合条件，错误信息: {error_el.text}")
        # 关闭错误提示
    except Exception:
        print(f"姓名: {name}, 身份证号: {id_number} 认证通过或未检测到错误提示")
    # 可根据实际流程决定是否需要返回或重置页面

print(">>>>>>>>> 已结束实名认证流程")


