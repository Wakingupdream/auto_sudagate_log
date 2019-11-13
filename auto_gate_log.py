from selenium import webdriver # 从selenium导入webdriver
'''每隔五个小时登录网关'''
import time
while(1):
	
	driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
	driver.get('http://a.suda.edu.cn/')


	name = driver.find_element_by_name("username")
	name.send_keys("20174227023")#输入学号
	pw = driver.find_element_by_name("password")
	pw.send_keys("")#输入密码

	login_button=driver.find_element_by_id('login')
	login_button.click()
	time.sleep(18000)
	login_button = driver.find_element_by_id('logout')
	login_button.click()
	


