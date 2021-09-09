import time

from selenium import webdriver
wd = webdriver.Chrome()
wd.get('http://120.79.172.137/pages/manfacturemodule/bom/query')

# 根据BOM编码查询
wd.find_element_by_class_name('ant-input.ng-tns-c109-0.ng-untouched.ng-pristine.ng-valid').send_keys('6\n')
time.sleep(3)
wd.find_element_by_class_name('ant-btn.ant-btn-primary').click()
