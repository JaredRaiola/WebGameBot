from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("https://www.sporcle.com/games/jaun/clickable-1-100-mines")

time.sleep(10)

browser.find_element_by_id("button-play").click()

time.sleep(1)

for i in range(100):
	# time.sleep(2) ## uncomment to slow down completion
	browser.find_element_by_id("slot{}".format(i)).click()

print("Done!")