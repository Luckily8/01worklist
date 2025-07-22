import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from utils.AppiumUtils import AppiumUtils as AU
from utils import load_yaml


data_file = "data/testcase1_data.yaml" # 测试数据文件路径
data_index = "companion_account1"  # 使用哪一组普通账号数据

# (可选)导入相关数据
test_data = load_yaml(data_file)
mobile = test_data[data_index].get("mobile", "17718846133")  
password = test_data[data_index].get("password", "01ai@12345678")

@pytest.mark.order(2)
@pytest.mark.parametrize("mobile,password", [(mobile, password)])
def test_change_password(mobile, password):
    """测试重置密码流程"""
    try:
        AU.return_to_home()
        AU.wait_and_log_then_click( "com.mix.upup:id/llMine", log_msg="我的页面")
        AU.wait_and_log_then_click( "com.mix.upup:id/tvSetting", log_msg="设置页面")
        AU.wait_and_log_then_click("com.mix.upup:id/tvSecurity", log_msg="账号安全页面")
        AU.wait_and_log_then_click("com.mix.upup:id/tvPassword", log_msg="密码页面")
        AU.wait_and_log("com.mix.upup:id/etPhone", log_msg="手机号输入框").send_keys(mobile)
        AU.wait_and_log_then_click("com.mix.upup:id/mcvNext", log_msg="下一步按钮")
        AU.sms_code_input()         # 输入验证码
        AU.wait_and_log_then_click("com.mix.upup:id/tvNext", log_msg="点击下一步按钮")
        AU.wait_and_log("com.mix.upup:id/etNewPassword", log_msg="新密码输入框").send_keys(password)
        AU.wait_and_log("com.mix.upup:id/etPasswordAgain", log_msg="确认密码输入框").send_keys(password)
        AU.wait_and_log_then_click("com.mix.upup:id/mcvNext", log_msg="下一步按钮")
        AU.save_screenshot("重置密码")  # 及时截图查看toast提示
    except Exception:
        AU.save_screenshot("流程失败")
    try:
        el_mine = AU.wait_and_log_then_click("com.mix.upup:id/llMine", log_msg="我的页面")
        assert el_mine is not None
    except AssertionError:
        pytest.fail("断言失败：未找到我的页面元素")

if __name__ == "__main__":
    pytest.main([__file__])

