import os
import pytest


if __name__ == '__main__':
    pytest.main(['./testcases/sales/order','--alluredir','./temp'])
    os.system('allure generate ./temp -o ./report --clean')