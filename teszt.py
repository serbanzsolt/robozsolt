from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import org.openqa.selenium.support.ui.Select

#---LOGIN---
PATH = "C:\Python\Projects\robozsolt\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#---FULLSCREEN---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://mmr.kh.gov.hu/MMR-PROD/?ACTION=BEJELENTESEK")

time.sleep(5)

userName = driver.find_element_by_name("Ecom_User_ID")
userName.send_keys("serbanz")

passWord = driver.find_element_by_name("Ecom_Password")
passWord.send_keys("Zsserban19851016")
passWord.send_keys(Keys.RETURN)

#---BEJELENTÉSEK---
try:
	tickets = WebDriverWait(driver, 300).until(
			EC.presence_of_element_located((By.LINK_TEXT,"Bejelentések"))
			#EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]"))
		)

	tickets.click()
	time.sleep(15)
except :
	driver.quit()


# ---ÚJ JEGY---
try:
	"""
	newTicket = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[5]/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div/div/div/a[1]"))
		)
	newTicket.click()
	"""
	newTicket = WebDriverWait(driver, 150).until(
			#EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[5]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/a"))
			EC.presence_of_element_located((By.LINK_TEXT,"Új bejelentés"))
		)
	newTicket.click()
except :
	driver.quit()

#---KITÖLTÉS---	

try:
	#---KATEGÓRIA---
	category = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.CLASS_NAME,"button-counter.required.empty"))
			#EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div[2]"))
		)
	category.click()
	time.sleep(3)
	
	category2 = driver.find_element_by_class_name("tree-text-search.form-control")
	#driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	category2.send_keys("hálózat")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Informatikai hálózat monitorozása")
	category3.click()
	time.sleep(3)

	#---TÁRGY---
	subject = driver.find_element_by_class_name("form-control.TextBox.required.empty")
	#driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("A II. Kerületi Népegészségügy hálózati ellenőrzése:")
	time.sleep(3)

	#---LEÍRÁS---
	description = driver.find_element_by_class_name("form-control.textarea.required.empty")
	description.click()
	time.sleep(3)
	#driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("A II. Kerületi Népegészségügy hálózati ellenőrzése:")
	description.send_keys(Keys.RETURN)
	description.send_keys("- Internet elérése a munkaállomásokon")
	description.send_keys(Keys.RETURN)
	description.send_keys("- Mappelt hálózati meghajtók elérése a munkaállomásokon")
	time.sleep(3)
	
	#---HELYSZÍN---
	location1 = driver.find_element_by_class_name("button-counter.empty")
	#driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/span")
	location1.click()
	time.sleep(3)

	location2 = driver.find_element_by_class_name("tree-text-search.form-control")
	#driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	location2.send_keys("szent imre")
	time.sleep(3)

	location3 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[1]/div/div[1]/span[2]")
	#find_element_by_name("1211 Budapest,  Szent Imre tér 3. 210228 hrsz. kivett óvoda")
	#driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[1]/div/div[1]/span[2]/span")
	location3.click()
	time.sleep(3)

	#---BEJELENTŐ---
	
	dotdotdot = driver.find_element_by_class_name("tags-input-arrow")
	#driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[8]/div[2]/div/div/div/div/div[2]")
	dotdotdot.click()
	time.sleep(3)
	

	requester = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div[1]/div[2]/div/div/div[3]/div/div/div[1]/div[2]/div[8]/div[2]/div/div/div/div/div/div[1]/div[2]/div/input")
	#driver.find_element_by_class_name("select__value-container.select__value-container--is-multi select__value-container--has-value.css-1mqctoc")
	#driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[8]/div[2]/div/div/div/div/div[1]/div[2]/div/input")
	requester.send_keys("Demus Lilla")
	time.sleep(3)
	requester.send_keys(Keys.RETURN)
	time.sleep(3)
	
	#---DÁTUM---

	date1 = driver.find_element_by_class_name("react-datepicker__input-container")
	time.sleep(3)
	date1.click()
	time.sleep(3)

	date2 = driver.find_element_by_class_name("time-selector.form-control.TextBox.date-picker.empty.react-datepicker-ignore-onclickoutside")
	date2.send_keys("2021.03.30")
	time.sleep(3)
	date2.send_keys(Keys.RETURN)
	time.sleep(3)

	#---BEJELENT---
	"""
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	time.sleep(20)
	"""
	print("Siker")

except :
	print("Nem sikerült")
	driver.quit()