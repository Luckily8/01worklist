from utils.AppiumUtils import AppiumUtils

# 替换为实际测试手机号 19812056630\13726927258(陪玩)\17718846133
user_phone = "19812056630" 

wait_and_log = AppiumUtils.wait_and_log
wait_and_log_then_click = AppiumUtils.wait_and_log_then_click
return_to_home = AppiumUtils.return_to_home
sms_code_input = AppiumUtils.sms_code_input
drag_copilot_and_quit_youth = AppiumUtils.drag_copilot_and_quit_youth
# 返回首页
return_to_home()
el3 = wait_and_log_then_click( "com.mix.upup:id/llMine", log_msg="我的页面")
el4 = wait_and_log_then_click( "com.mix.upup:id/tvSetting", log_msg="设置页面")
el5 = wait_and_log_then_click( "com.mix.upup:id/tvLogout", log_msg="登出按钮")
el6 = wait_and_log_then_click( "com.mix.upup:id/dialog_alert_two_confirm", log_msg="弹窗确认按钮")
el7 = wait_and_log_then_click( "com.mix.upup:id/cvPhoneLogin", log_msg="手机号登录按钮")
el8 = wait_and_log("com.mix.upup:id/etPhone", log_msg="手机号输入框").send_keys(user_phone)
el9 = wait_and_log_then_click("com.mix.upup:id/tvLoginOrRegister", log_msg="登录/注册按钮")
el10 = wait_and_log_then_click("com.mix.upup:id/dialog_alert_two_confirm", log_msg="弹窗确认按钮")
el11 = wait_and_log_then_click("com.mix.upup:id/tvLoginOrRegister", log_msg="登录/注册按钮")
# 输入验证码
sms_code_input()
el12 = wait_and_log_then_click("com.mix.upup:id/tvNext", log_msg="点击下一步按钮")

print(">>>>>>>> 已结束换号验证码登录流程")
