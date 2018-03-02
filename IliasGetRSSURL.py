from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from IliasLogin import login
import os


RSS_URL = open('rssfeed.txt', 'r+')


if(os.stat("rssfeed.txt").st_size == 0):

	#Paths for chrome Drivers
	CHROME_PATH = '/usr/bin/google-chrome'
	CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
	
	chrome_options = Options()  
	chrome_options.add_argument("--headless")  
	chrome_options.binary_location = CHROME_PATH
	
	driver = webdriver.Chrome(
	       executable_path=CHROMEDRIVER_PATH,
	       chrome_options=chrome_options
	   )
	
	#Login into your Ilias-Page
	
	login(driver)
	
	#navigate to your RSS-URL
	
	RSSButton = driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilTabsContentOuter']/div[@id='ilContentContainer']/div[@class='row']/div[@id='il_right_col']/div[@id='block_pdnews_0']/div[@class='il_Block']/div[@class='ilBlockInfo ilLeft']/a/span[@class='ilNewsRssIcon']")
	RSSButton.click()
	RSS = driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilTabsContentOuter']/div[@id='ilContentContainer']/div[@class='row']/div[@id='il_center_col']/div[@id='block_pdcontent_0']/div[@class='il_Block']/div[@class='ilBlockContent']/p[3]/a[@class='small']")
	
	rsstxt = RSS.get_attribute("href")
	#Store personal RSS-URL in a .txt file
	RSS_URL.write(rsstxt)
	RSS_URL.close()
	driver.close()
else :
	print ("RSS-Link already downloaded: " + RSS_URL.readline())