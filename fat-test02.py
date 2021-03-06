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

	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	# 1. ZSOLT - VÁRADI symantec
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---BEJELENTÉSEK---
try:
	tickets = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]"))
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
	category2.send_keys("vírusvédelem")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Informatikai vírusvédelem monitorozása")
	category3.click()

	#---TÁRGY---
	subject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("Symantec Vírusvédelem ellenőrzése")

	#---LEÍRÁS---
	description = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("Symantec Vírusvédelem ellenőrzése a II. Kerületi Népegészségügyi gépeken")
	
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
	
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	time.sleep(20)

except :
	driver.quit()

	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	# 2. ZSOLT - PODMANICZKY adatmentés
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---BEJELENTÉSEK---
try:
	tickets = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]"))
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
	category2.send_keys("vírusvédelem")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Informatikai vírusvédelem monitorozása")
	category3.click()

	#---TÁRGY---
	subject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("Symantec Vírusvédelem ellenőrzése")

	#---LEÍRÁS---
	description = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("Symantec Vírusvédelem ellenőrzése a VI. Kerületi Népegészségügyi gépeken")
	
	#---HELYSZÍN---
	location1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/span")
	location1.click()
	time.sleep(3)

	location2 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	location2.send_keys("podmani")
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
	
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	time.sleep(20)

except :
	driver.quit()

	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	# 3. SZILÁRD - KOSSUTH TÉR adatmentés
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---BEJELENTÉSEK---
try:
	tickets = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]"))
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
	category2.send_keys("vírusvédelem")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Informatikai vírusvédelem monitorozása")
	category3.click()

	#---TÁRGY---
	subject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("Symantec Vírusvédelem ellenőrzése")

	#---LEÍRÁS---
	description = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("Symantec Vírusvédelem ellenőrzése a V. Kerületi Népegészségügyi gépeken")
	
	#---HELYSZÍN---
	location1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/span")
	location1.click()
	time.sleep(3)

	location2 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	location2.send_keys("kossuth")
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
	
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	time.sleep(20)

except :
	driver.quit()

	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	# 4. SZILÁRD - BÁNKI adatmentés
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---BEJELENTÉSEK---
try:
	tickets = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]"))
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
	category2.send_keys("vírusvédelem")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Informatikai vírusvédelem monitorozása")
	category3.click()

	#---TÁRGY---
	subject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("Symantec Vírusvédelem ellenőrzése")

	#---LEÍRÁS---
	description = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("Symantec Vírusvédelem ellenőrzése a XIV. Kerületi Népegészségügyi gépeken")
	
	#---HELYSZÍN---
	location1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/span")
	location1.click()
	time.sleep(3)

	location2 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	location2.send_keys("bánki")
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
	
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	time.sleep(20)

except :
	driver.quit()

	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	# 5. ANDRÁS - BUDAFOKI adatmentés
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---BEJELENTÉSEK---
try:
	tickets = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]"))
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
	category2.send_keys("vírusvédelem")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Informatikai vírusvédelem monitorozása")
	category3.click()

	#---TÁRGY---
	subject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("Symantec Vírusvédelem ellenőrzése")

	#---LEÍRÁS---
	description = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("Symantec Vírusvédelem ellenőrzése a XI. Kerületi Népegészségügyi gépeken")
	
	#---HELYSZÍN---
	location1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/span")
	location1.click()
	time.sleep(3)

	location2 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	location2.send_keys("budafoki")
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
	
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	time.sleep(20)

except :
	driver.quit()

	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	# 6. ANDRÁS - NFO adatmentés
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	#---BEJELENTÉSEK---
try:
	tickets = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]"))
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
	category2.send_keys("vírusvédelem")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Informatikai vírusvédelem monitorozása")
	category3.click()

	#---TÁRGY---
	subject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("Symantec Vírusvédelem ellenőrzése")

	#---LEÍRÁS---
	description = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("Symantec Vírusvédelem ellenőrzése a Népegészségügyi Főosztály gépein")
	
	#---HELYSZÍN---
	location1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/span")
	location1.click()
	time.sleep(3)

	location2 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	location2.send_keys("váci út 172")
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
	
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	time.sleep(20)

except :
	driver.quit()

	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	# 7. DANI - FOKOS adatmentés
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---BEJELENTÉSEK---
try:
	tickets = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]"))
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
	category2.send_keys("vírusvédelem")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Informatikai vírusvédelem monitorozása")
	category3.click()

	#---TÁRGY---
	subject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("Symantec Vírusvédelem ellenőrzése")

	#---LEÍRÁS---
	description = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("Symantec Vírusvédelem ellenőrzése a X. Kerületi Népegészségügyi gépeken")
	
	#---HELYSZÍN---
	location1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/span")
	location1.click()
	time.sleep(3)

	location2 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	location2.send_keys("fokos")
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
	
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	time.sleep(20)

except :
	driver.quit()

	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	# 8. DANI - SZENT IMRE adatmentés
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---BEJELENTÉSEK---
try:
	tickets = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/nav/ul[1]/li[2]"))
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
	category2.send_keys("vírusvédelem")
	time.sleep(3)
	
	category3 = driver.find_element_by_id("Informatikai vírusvédelem monitorozása")
	category3.click()

	#---TÁRGY---
	subject = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/div/input")
	subject.send_keys("Symantec Vírusvédelem ellenőrzése")

	#---LEÍRÁS---
	description = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[5]/div/div/div/textarea")
	description.send_keys("Symantec Vírusvédelem ellenőrzése a XXI. Kerületi Népegészségügyi gépeken")
	
	#---HELYSZÍN---
	location1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div[2]/div[6]/div[1]/div/div/div[2]/span")
	location1.click()
	time.sleep(3)

	location2 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[1]/div/input")
	location2.send_keys("szent imre")
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
	
	sendButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]")
	sendButton.click()
	time.sleep(20)

except :
	driver.quit()

	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
