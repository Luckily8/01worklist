import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from utils.AppiumUtils import AppiumUtils as AU
from utils import load_yaml

data_file = "data/testcase1_data.yaml" # 测试数据文件路径
data_index = "companion_account1"  # companion_account1 normal_account1

# (可选)导入相关数据
test_data = load_yaml(data_file)
mobile = test_data[data_index].get("mobile", "17718846133")  

@pytest.mark.order(2)
@pytest.mark.parametrize("mobile", [mobile])
def test_change_user(mobile):
    """测试切换用户流程"""
    try:
        AU.return_to_home()
        AU.wait_and_log_then_click( "com.mix.upup:id/llMine", log_msg="我的页面")
        AU.wait_and_log_then_click( "com.mix.upup:id/tvSetting", log_msg="设置页面")
        AU.wait_and_log_then_click( "com.mix.upup:id/tvLogout", log_msg="登出按钮")
        AU.wait_and_log_then_click( "com.mix.upup:id/dialog_alert_two_confirm", log_msg="弹窗确认按钮")
        AU.wait_and_log_then_click( "com.mix.upup:id/cvPhoneLogin", log_msg="手机号登录按钮")
        AU.wait_and_log("com.mix.upup:id/etPhone", log_msg="手机号输入框").send_keys(mobile)
        AU.wait_and_log_then_click("com.mix.upup:id/tvLoginOrRegister", log_msg="登录/注册按钮")
        AU.wait_and_log_then_click("com.mix.upup:id/dialog_alert_two_confirm", log_msg="弹窗确认按钮")
        AU.wait_and_log_then_click("com.mix.upup:id/tvLoginOrRegister", log_msg="登录/注册按钮")
        # 输入验证码
        AU.sms_code_input()
        AU.wait_and_log_then_click("com.mix.upup:id/tvNext", log_msg="点击下一步按钮")
        AU.save_screenshot("换号")  # 及时截图        
        # AU.drag_copilot_and_quit_youth()  # 青少年模式复杂,每日手点一次即可

    except Exception:
        AU.save_screenshot("流程中失败")
    try:
        el_mine = AU.wait_and_log_then_click("com.mix.upup:id/llMine", log_msg="我的页面")
        assert el_mine is not None
    except AssertionError:
        pytest.fail("断言失败：未找到我的页面元素")

if __name__ == "__main__":
    pytest.main([__file__])

