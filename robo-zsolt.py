from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import org.openqa.selenium.support.ui.Select

#---LOGIN---
PATH = "C:\Python\chromedriver.exe"
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
	tickets = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]/a"))
		)

	tickets.click()
	time.sleep(10)
except :
	driver.quit()


# ---ÚJ JEGY---
try:
	newTicket = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[5]/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div/div/div/a[1]"))
		)
	newTicket.click()
except :
	driver.quit()

#---KITÖLTÉS---	

try:
	#---KATEGÓRIA---
	category = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div[2]"))
		)
	category.click()
	time.sleep(3)
	
	category2 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	category2.send_keys("adat")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Egyéb adatvédelemmel kapcsolatos")
	category3.click()

	#---TÁRGY---
	subject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("Napi adatmentés ellenőrzése")

	#---LEÍRÁS---
	description = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("Napi adatmentés ellenőrzése a II. Kerületi Népegészségügy hálózati meghajtójáról")
	
	#---HELYSZÍN---
	location1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/span")
	location1.click()
	time.sleep(3)

	location2 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	location2.send_keys("váradi")
	time.sleep(3)

	location3 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[1]/div/div[1]/span[2]/span")
	location3.click()

	#---BEJELENTŐ---
	
	dotdotdot = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[8]/div[2]/div/div/div/div/div[2]")
	dotdotdot.click()
	time.sleep(3)

	requester = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[8]/div[2]/div/div/div/div/div[1]/div[2]/div/input")
	requester.send_keys("Demus Lilla")
	time.sleep(3)
	requester.send_keys(Keys.RETURN)
	time.sleep(3)
	
	#---BEJELENT---
	"""
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	"""

except :
	driver.quit()