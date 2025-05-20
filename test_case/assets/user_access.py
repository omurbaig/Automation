import time
from telnetlib import STATUS
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.maximize_window()
textbox_username_name="username"
username="Admin"
driver.find_element(By.NAME, textbox_username_name).send_keys(username)
textbox_password_name="password"
password="admin123"
driver.find_element(By.NAME,textbox_password_name).send_keys(password)
time.sleep(5)
btn_login_xpath="//button[@type='submit']"
driver.find_element(By.XPATH, btn_login_xpath).click()
time.sleep(5)
sidepanel_admin_xpath="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
driver.find_element(By.XPATH, sidepanel_admin_xpath).click()
time.sleep(10)
#driver.find_element(By.XPATH , "(//input[contains(@class, 'oxd-input oxd-input--active')])[2]").send_keys("Bsstest2")
#time.sleep(5)
#dropdown = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
#time.sleep(5)
#dropdown.click()
#time.sleep(5)
#element = driver.find_element(By.XPATH, "//div[@role='option'][2]").click()
#time.sleep(5)
#item=(driver.find_element(By.XPATH ,"//input[@placeholder='Type for hints...']"))
#time.sleep(5)
#item.send_keys("San")
#time.sleep(5)
#abc=driver.find_element(By.XPATH, "//div[@role='option'][1]")
#time.sleep(5)
#abc.click()
#time.sleep(10)
#dropdown = driver.find_element(By.XPATH, "(//div[contains(@class, 'oxd-select-text-input')])[2]")
#time.sleep(5)
#dropdown.click()
#time.sleep(5)
# Admin - user management

#test= driver.find_element(By.XPATH, "//div[@role='option'][3]")
#time.sleep(5)
#test.click()
#time.sleep(5)
#search_btn_type="//*[@type='submit']"
#driver.find_element(By.XPATH , search_btn_type).click()
#time.sleep(5)
btn_edit_xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/button[2]/i[1]"
driver.find_element(By.XPATH , btn_edit_xpath).click()
time.sleep(5)
dropdown_userrole_xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"
#driver.find_element(By.XPATH ,user_role_dropdown_xpath).click()
time.sleep(5)
select_dropdown_userrole_xpath="//div[@role='option'][2]"
#user_role_select= driver.find_element(By.XPATH ,user_role_dropdown_edit_xpath)
time.sleep(5)
#user_role_select.click()
user_role_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, dropdown_userrole_xpath)))
time.sleep(10)
user_role_field.click()

select_role_field = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH,select_dropdown_userrole_xpath))
)
time.sleep(5)
select_role_field.click()

time.sleep(5)
status_dropdown_xpath="//label[contains(text(),'Status')]/following::div[contains(@class, 'oxd-select-text')][1]"
driver.find_element(By.XPATH ,status_dropdown_xpath).click()
time.sleep(5)
status_dropdown_edit_xpath="//div[@role='option'][3]"
status_select= driver.find_element(By.XPATH ,status_dropdown_edit_xpath)
time.sleep(5)
status_select.click()
time.sleep(5)
textbox_employeename_xapth="//input[@placeholder='Type for hints...']"
element = driver.find_element(By.XPATH ,textbox_employeename_xapth)
time.sleep(10)
element.clear()
time.sleep(10)
element = driver.find_element(By.XPATH, "//div[@role='option'][3]").click()
element = driver.find_element(By.XPATH ,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span")
time.sleep(5)
element.click()
time.sleep(5)
dropdown = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]//li[4]")
time.sleep(5)
dropdown.click()
time.sleep(10)