# 生成测试报告
# allure 测试报告

# 执行用例
import os
import pytest

if __name__ == '__main__':
    # 执行用例生成测试报告
    pytest.main(['-s','./test_case/test_case.py','--alluredir','./allure-results'])
    # 生成测试报告
    os.system('allure generate ./allure-results -o ./allure-reports')