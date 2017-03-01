from splinter.browser import Browser
from time import sleep
import traceback


# b = Browser(driver_name = 'chrome')
b = Browser(driver_name = 'firefox')

# b.visit("http://www.google.com")

username = u"11452133"

password = u"714001"


''' cookie value of starts and ends '''

starts = u"%u4E0A%u6D77%2CSHH"
ends = u"%u8425%u53E3%u4E1C%2CYGT"

# time format
dtime = u"2016-02-01"

# student names
pa = u"李乾豪"


# set urls
system_frontpage_url = "http://lib.tongji.edu.cn/clientweb/xcus/ic2/Default.aspx"

b.visit(system_frontpage_url)
b.driver.set_window_size(1920, 1080)

def login():
	b.find_by_text(u"登录").click()
	sleep(3)
	b.fill("id", username)
	sleep(1)
	b.fill("pwd", password)
	sleep(1)
	print(u"loading...")

login()