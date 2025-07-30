import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from utils.AppiumUtils import AppiumUtils as AU
from utils import load_yaml
from pages.login_page import LoginPage

data_file = "data/testcase1_data.yaml"
data_index = "normal_account1"
# data_index = "companion_account1"
test_data = load_yaml(data_file)
mobile = test_data[data_index].get("mobile", "17718846133")

@pytest.mark.order(1)
@pytest.mark.parametrize("mobile", [mobile])
def test_login_with_mobile_and_sms(mobile):
    """POM风格模拟手机号登录流程"""
    driver = AU.driver  # 获取全局driver
    login_page = LoginPage(driver)
    try:
        login_page.login_flow(mobile, AU.sms_code_input)
        AU.save_screenshot("登录")
        login_page.assert_mine_page()
    except Exception:
        pytest.fail("断言失败：未找到我的页面元素")

if __name__ == "__main__":
    pytest.main([__file__])
