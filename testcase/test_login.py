import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from utils.AppiumUtils import AppiumUtils as AU
from utils import load_yaml

# (可选)导入相关数据
test_data = load_yaml("data/testcase1_data.yaml")
mobile = test_data["normal_account1"].get("mobile", "17718846133")  # 未找到则使用默认手机号

@pytest.mark.order(1)
@pytest.mark.parametrize("mobile", [mobile])
def test_login_with_mobile_and_sms(mobile):
    """模拟手机号登录流程"""
    try:
        AU.wait_and_log_then_click("com.mix.upup:id/cvPhoneLogin", log_msg="手机号登录按钮")
        AU.wait_and_log("com.mix.upup:id/etPhone", log_msg="手机号输入框").send_keys(mobile)
        AU.wait_and_log_then_click("com.mix.upup:id/tvLoginOrRegister", log_msg="登录/注册按钮")
        AU.wait_and_log_then_click("com.mix.upup:id/dialog_alert_two_confirm", log_msg="弹窗确认按钮")
        AU.wait_and_log_then_click("com.mix.upup:id/tvLoginOrRegister", log_msg="验证码输入按钮")
        AU.sms_code_input()
        AU.wait_and_log_then_click("com.mix.upup:id/tvNext", log_msg="点击下一步按钮")

        # AU.drag_copilot_and_quit_youth() 青少年模式复杂,每日手点一次即可
        AU.save_screenshot("tets_login") # 及时截图查看toast提示
        # 断言：页面出现 id 为 com.mix.upup:id/tvGame 的元素
        el_mine = AU.wait_and_log("com.mix.upup:id/llMine", log_msg="我的页面")
        assert el_mine is not None
        el_mine.click()  # 点击进入我的页面
    except Exception:
        pytest.fail("断言失败：未找到我的页面元素")

if __name__ == "__main__":
    pytest.main([__file__])



