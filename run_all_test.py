import os
import sys
import time

# 添加项目根目录到 sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_allure_report():
    print("======开始执行！！！======")
    curpath = os.path.dirname(os.path.realpath(__file__))
    allure_results_dir = os.path.join(curpath, "reports", "allure-results")
    allure_report_dir = os.path.join(curpath, "reports", "allure-report")
    test_dir = os.path.join(curpath, "testcase")
    if not os.path.exists(allure_results_dir):
        os.makedirs(allure_results_dir)
    if not os.path.exists(allure_report_dir):
        os.makedirs(allure_report_dir)
    # 日志目录也保证存在
    log_dir = os.path.join(curpath, "log")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    # 运行pytest生成allure原始结果
    cmd1 = f"set PYTHONPATH={curpath} && pytest {test_dir} --alluredir={allure_results_dir}"
    print(f"运行命令: {cmd1}")
    os.system(cmd1)
    # 生成并打开allure报告
    cmd2 = f"allure generate {allure_results_dir} -o {allure_report_dir} --clean"
    print(f"生成Allure报告: {cmd2}")
    os.system(cmd2)
    cmd3 = f"allure open {allure_report_dir}"
    print(f"打开Allure报告: {cmd3}")
    os.system(cmd3)
    print("测试已全部完成, 可在浏览器查看Allure报告")
    print("======执行结束！！！======")

if __name__ == "__main__":
    run_allure_report()