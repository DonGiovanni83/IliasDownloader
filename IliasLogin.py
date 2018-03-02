from selenium import webdriver
from selenium.webdriver.common.keys import Keys

UserID = open('userId.txt', 'r')
 
def read_linenumber(file,x):
	for index, line in enumerate(iter(file)):
		if index+1 == x:
			return line[:-1]
	return None

print "Please enter your Ilias-Username : "
IliasUsername = raw_input()
print "Please enter your Ilias-Password : "
IliasPassword = raw_input() 

print "Logging in to Ilias"

options = webdriver.ChromeOptions()
options.add_argument('headless')
Driver = webdriver.Chrome(chrome_options=options)

def login(Driver):
	Driver.get("https://www.ilias.unibe.ch")
	SelectUni = Driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilStartupSection']/div[@id='wayf_div']/form[@id='IdPList']/span[@id='user_idp_iddwrap']/input[@id='user_idp_iddtext']")
	SelectUni.clear()
	SelectUni.send_keys('bern')
	SelectUni.send_keys(Keys.RETURN)

	Driver.get_screenshot_as_file("/home/fabio/Documents/P1/iliasLogin3.1.png")

	LoginUni = Driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilStartupSection']/div[@id='wayf_div']/form[@id='IdPList']/input[@id='wayf_submit_button']")
	LoginUni.click()


	Driver.find_element_by_css_selector('#username').send_keys(IliasUsername)
	Driver.find_element_by_css_selector('#password').send_keys(IliasPassword)
	LoginButton = Driver.find_element_by_xpath("/html/body/div[@class='aai_box']/div[@class='aai_login_field']/form/div[4]/button[@class='aai_login_button']")

	Driver.get_screenshot_as_file("/home/fabio/Documents/P1/iliasLogin3.2.png")

	LoginButton.click()

	Driver.get_screenshot_as_file("/home/fabio/Documents/P1/iliasLogin3.3.png")

Driver.close()
