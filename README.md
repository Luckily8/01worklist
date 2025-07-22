# 01worklist

## 项目简介
本项目为 Appium + pytest 的移动端 UI 自动化测试框架，支持多账号、多场景、数据驱动、自动生成测试报告。

## 目录结构建议
```
autoRun/
  testcase/         # 测试用例（pytest风格，test_开头）
  utils/            # 公共工具类（如AppiumUtils、数据处理等）
  data/             # 测试数据（yaml/json格式）
  config/           # 配置文件（如设备、环境、账号等）
  report/           # 测试报告（pytest-html或Allure）
  logs/             # 日志文件
  commont/          # 公共模块（如日志、报告封装）
  requirements.txt  # 依赖管理
  run_all_test.py   # 一键运行入口
  README.md         # 项目说明
```

## 依赖安装
```bash
pip install -r requirements.txt
```

## 运行方式
- 推荐在项目根目录下运行：
```bash
python run_all_test.py
```
- 支持 pytest-html 或 Allure 测试报告。

## 测试用例规范
- 用例文件以 test_ 开头，函数以 test_ 开头。
- 推荐使用 pytest.mark.order 控制业务流程顺序。
- 用例中断言失败自动截图，报告中展示。
- 测试数据、账号、密码等全部放在 data/ 或 config/，用 yaml/json 管理。

## 工具类建议
- AppiumUtils 统一管理 driver，所有方法参数统一（by, value, timeout, log_msg）。
- 支持多种定位方式，异常处理和日志输出。
- 所有断言失败自动截图。

## 日志与报告
- 日志用 logging 标准库，分级输出到 logs/。
- 测试报告推荐 Allure，支持详细步骤、截图、参数、附件。

## CI/CD 集成
- 可集成 Jenkins、GitHub Actions 等平台，实现自动化测试、报告推送、结果通知。

## 代码质量
- 推荐 flake8、black 做代码格式检查和自动化格式化。
- 适当增加注释和 README 文档，说明项目结构、用例编写规范、运行方式。

## 依赖管理
- 用 requirements.txt 管理所有依赖，方便环境迁移和重建。

## 失败截图与断言
- 所有断言失败时自动截图，报告中展示截图，便于定位问题。

## 业务流程自动化
- 用 pytest-order 或文件名前缀控制用例执行顺序，保证业务流程完整。

---
如需具体某一项的自动化改造或代码示例，请联系维护者。
