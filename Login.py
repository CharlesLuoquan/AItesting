#-*- coding: UTF-8 -*-
from selenium import webdriver
import time
# import os  
# import logging  
# import subprocess  

browser = webdriver.Chrome(executable_path = 'F:\python\chromedriver.exe')
browser.get("http://document.inkwork.cn/login.html")
time.sleep(1)
# browser.find_element_by_link_text("登录").click()
# time.sleep(1)
browser.find_element_by_id("user_mobilephone_text").send_keys("18500000002")
browser.find_element_by_id("user_loginpass_text").send_keys("123456")
browser.find_element_by_id("user-login").click()
time.sleep(1)
# browser.find_element_by_link_text("搜索内容、文件、作者...").send_keys(u'时讯汇')

  
# log = logging.getLogger("Core.Analysis.Processing")  
#   
# INTERPRETER = "F:\python"  
#   
#   
# if not os.path.exists(INTERPRETER):  
#     log.error("Cannot find INTERPRETER at path \"%s\"." % INTERPRETER)  
#       
# processor = "search.py"  
#   
# pargs = [INTERPRETER, processor]  
# pargs.extend(["--input=inputMd5s"])  
# subprocess.Popen(pargs)
# 
# try:
#     if browser.find_element_by_link_text("退出"):
#         print "Login Successfully."
# except:
#     print "Login failed."
# #browser.quit()