from selenium.webdriver.common.keys import Keys
import getpass

def login(Driver):
	
	print "Please enter your Ilias-Username : "
	IliasUsername = raw_input()
	print "Please enter your Ilias-Password : "
	IliasPassword = getpass.getpass() 



	print "Logging in to Ilias"

	#Select UniBern in Ilias
	Driver.get("https://www.ilias.unibe.ch")
	SelectUni = Driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilStartupSection']/div[@id='wayf_div']/form[@id='IdPList']/span[@id='user_idp_iddwrap']/input[@id='user_idp_iddtext']")
	SelectUni.clear()
	SelectUni.send_keys('bern')
	SelectUni.send_keys(Keys.RETURN)

	LoginUni = Driver.find_element_by_xpath("/html/body[@class='std']/div[@id='ilAll']/div[@id='mainspacekeeper']/div[@class='row']/div[@id='fixed_content']/div[@id='mainscrolldiv']/div[@class='ilStartupSection']/div[@id='wayf_div']/form[@id='IdPList']/input[@id='wayf_submit_button']")
	LoginUni.click()

	#Switch Login
	Driver.find_element_by_css_selector('#username').send_keys(IliasUsername)
	Driver.find_element_by_css_selector('#password').send_keys(IliasPassword)
	LoginButton = Driver.find_element_by_xpath("/html/body/div[@class='aai_box']/div[@class='aai_login_field']/form/div[4]/button[@class='aai_login_button']")


	LoginButton.click()
	#now on Ilias Home Page

