from selenium import webdriver
from selenium.webdriver.common.keys import Keys

UserID = open('userId.txt', 'r')
RSS_URL = open('rssfeed.txt', 'r+')
 
def read_linenumber(file,x):
	for index, line in enumerate(iter(file)):
		if index+1 == x:
			return line[:-1]
	return None

IliasUsername = read_linenumber(UserID, 2)
IliasPassword = read_linenumber(UserID, 2)

print "Logging in to Ilias"

options = webdriver.ChromeOptions()
options.add_argument('headless')
Driver = webdriver.Chrome(chrome_options=options)

Driver.get("https://www.ilias.unibe.ch")
SelectUni = Driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilStartupSection']/div[@id='wayf_div']/form[@id='IdPList']/span[@id='user_idp_iddwrap']/input[@id='user_idp_iddtext']")
SelectUni.clear()
SelectUni.send_keys('bern')
SelectUni.send_keys(Keys.RETURN)


LoginUni = Driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilStartupSection']/div[@id='wayf_div']/form[@id='IdPList']/input[@id='wayf_submit_button']")
LoginUni.click()


Driver.find_element_by_css_selector('#username').send_keys(IliasUsername)
Driver.find_element_by_css_selector('#password').send_keys(IliasPassword)
LoginButton = Driver.find_element_by_xpath("/html/body/div[@class='aai_box']/div[@class='aai_login_field']/form/div[4]/button[@class='aai_login_button']")

LoginButton.click()

RSSButton = Driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilTabsContentOuter']/div[@id='ilContentContainer']/div[@class='row']/div[@id='il_right_col']/div[@id='block_pdnews_0']/div[@class='il_Block']/div[@class='ilBlockInfo ilLeft']/a/span[@class='ilNewsRssIcon']")
RSSButton.click()

Driver.get_screenshot_as_file("RSSFeedPage.png")

RSS = Driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilTabsContentOuter']/div[@id='ilContentContainer']/div[@class='row']/div[@id='il_center_col']/div[@id='block_pdcontent_0']/div[@class='il_Block']/div[@class='ilBlockContent']/p[3]/a[@class='small']")


rsstxt = RSS.get_attribute("href")

RSS_URL.write(rsstxt)

RSS_URL.close()

Driver.close()
