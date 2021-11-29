import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---CSV FÁJL ADATAINAK MENTÉSE---
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
data = open("ticket2.csv", encoding='latin-1')

#---CSV MEGNYITÁS, ELLENŐRZÉS, DELIMITER VÁLTÁS

csv_data = csv.reader(data, delimiter=';')

data_lines = list(csv_data)

print("FEJLÉCEK: ", data_lines[0])
print("CSV fileban lévő elemek száma: ", len(data_lines))
print("\n"+"CSV TARTALMA")
for x in data_lines[1:]:
	print(x)

print("Egy adat:")
print(data_lines[1])
print("Type:", type(data_lines))

#--- ADATOK KIMENTÉSE:---

#---Sorszám---
number = []
for lines in data_lines[1:]:
	number.append(lines[0])

print("SORSZÁMOK:")
print(number)
#---Kategória keresés---

category_search = []
for lines in data_lines[1:]:
	category_search.append(lines[1])

print("KATEGÓRIA KERESÉSI SZAVAK:")
print(category_search)

#---Kategória kiválasztás---

category_exact = []
for lines in data_lines[1:]:
	category_exact.append(lines[2])

print("KATEGÓRIA:")
print(category_exact)

#---Tárgy---

ticket_subject = []
for lines in data_lines[1:]:
	ticket_subject.append(lines[3])

print("TÁRGY:")
print(ticket_subject)
#---Leírás 01---

description01 = []
for lines in data_lines[1:]:
	description01.append(lines[4])

print("LEÍRÁS01:")
print(description01)
#---Leírás 02---

description02 = []
for lines in data_lines[1:]:
	description02.append(lines[5])

print("LEÍRÁS02:")
print(description02)
#---Leírás 03---

description03 = []
for lines in data_lines[1:]:
	description03.append(lines[6])

print("LEÍRÁS03:")
print(description03)

#---Helyszín keresés---

location_search = []
for lines in data_lines[1:]:
	location_search.append(lines[7])

print("HELYSZÍN KERESÉS:")
print(location_search)
#---Bejelentő---

ticket_requester = []
for lines in data_lines[1:]:
	ticket_requester.append(lines[8])

print("BEJELENTŐ:")
print(ticket_requester)
#---DÁTUM---

request_date = []
for lines in data_lines[1:]:
	request_date.append(lines[9])

print("DÁTUM")
print(request_date)
"""
counter = 0
for tickets in data_lines[1:]:
	print(description01[counter])
	counter = counter+1
	pass
"""
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---LOGIN ÉS VÁLTÁS FULLSCREENRE---
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
#---BEJELENTÉS CIKLUS---
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

counter = 0
for tickets in data_lines[1:]:
	
#---BEJELENTÉSEK GOMB---
	try:
		tickets = WebDriverWait(driver, 300).until(
				EC.presence_of_element_located((By.LINK_TEXT,"Bejelentések"))
			)

		tickets.click()
		time.sleep(15)
	except :
		driver.quit()

	# ---ÚJ JEGY---
	try:
		newTicket = WebDriverWait(driver, 150).until(
				EC.presence_of_element_located((By.LINK_TEXT,"Új bejelentés"))
			)
		newTicket.click()
	except :
		driver.quit()

	#---JEGY KITÖLTÉS---	

	try:
		#---KATEGÓRIA---
		category = WebDriverWait(driver, 30).until(
				EC.presence_of_element_located((By.CLASS_NAME,"button-counter.required.empty"))
			)
		category.click()
		time.sleep(3)
		
		category2 = driver.find_element_by_class_name("tree-text-search.form-control")
		category2.send_keys(category_search[counter])
		time.sleep(3)
		
		category3 = driver.find_element_by_id(category_exact[counter])
		category3.click()
		time.sleep(3)

		#---TÁRGY---
		subject = driver.find_element_by_class_name("form-control.TextBox.required.empty")
		subject.send_keys(ticket_subject[counter])
		time.sleep(3)

		#---LEÍRÁS---
		description = driver.find_element_by_class_name("form-control.textarea.required.empty")
		description.click()
		time.sleep(3)
		description.send_keys(description01[counter])
		description.send_keys(Keys.RETURN)
		description.send_keys(description02[counter])
		description.send_keys(Keys.RETURN)
		description.send_keys(description03[counter])
		time.sleep(3)
		
		#---HELYSZÍN---
		location1 = driver.find_element_by_class_name("button-counter.empty")
		location1.click()
		time.sleep(3)

		location2 = driver.find_element_by_class_name("tree-text-search.form-control")
		location2.send_keys(location_search[counter])
		time.sleep(3)

		location3 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[1]/div/div[1]/span[2]")
		location3.click()
		time.sleep(3)

		#---BEJELENTŐ---
		
		dotdotdot = driver.find_element_by_class_name("tags-input-arrow")
		dotdotdot.click()
		time.sleep(3)
		
		requester = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[5]/div[1]/div[2]/div/div/div[3]/div/div/div[1]/div[2]/div[8]/div[2]/div/div/div/div/div/div[1]/div[2]/div/input")
		requester.send_keys(ticket_requester[counter])
		time.sleep(3)
		requester.send_keys(Keys.RETURN)
		time.sleep(3)
		
		#---DÁTUM---

		date1 = driver.find_element_by_class_name("react-datepicker__input-container")
		time.sleep(3)
		date1.click()
		time.sleep(3)

		date2 = driver.find_element_by_class_name("time-selector.form-control.TextBox.date-picker.empty.react-datepicker-ignore-onclickoutside")
		date2.send_keys(request_date[counter])
		time.sleep(3)
		date2.send_keys(Keys.RETURN)
		time.sleep(3)

		#---BEJELENT---
		
		sendButton = driver.find_element_by_class_name("btn.btn-default.Bekld")
		sendButton.click()
		time.sleep(20)
		
		print(counter+1, ". SZÁMÚ JEGY FELVÉTELE SIKERES!")

	except :
		print(counter+1, ". SZÁMÚ JEGY FELVÉTELE SIKERTELEN!")
		driver.quit()	

	counter = counter+1
	pass
