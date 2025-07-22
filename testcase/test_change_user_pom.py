import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from utils.AppiumUtils import AppiumUtils as AU
from utils import load_yaml
from pages.mine_page import MinePage
from pages.login_page import LoginPage

data_file = "data/testcase1_data.yaml"
data_index = "companion_account1"
test_data = load_yaml(data_file)
mobile = test_data[data_index].get("mobile", "17718846133")

@pytest.mark.order(2)
@pytest.mark.parametrize("mobile", [mobile])
def test_change_user_pom(mobile):
    """POM风格测试切换用户流程"""
    driver = AU.driver
    mine_page = MinePage(driver)
    login_page = LoginPage(driver)
    try:
        AU.return_to_home()
        mine_page.click_mine()
        mine_page.goto_setting()
        mine_page.goto_logout()
        mine_page.confirm_alert()
        login_page.click_phone_login()
        login_page.input_phone(mobile)
        login_page.click_login_or_register()
        login_page.click_alert_confirm()
        login_page.click_login_or_register()
        AU.sms_code_input()
        login_page.click_next()
        AU.save_screenshot("换号")
        mine_page.assert_mine_page()
    except Exception:
        AU.save_screenshot("流程中失败")
        pytest.fail("断言失败：未找到我的页面元素")

if __name__ == "__main__":
    pytest.main([__file__])
