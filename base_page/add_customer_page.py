import time
from selenium.webdriver.common.by import By

class add_customer_page:
    # Locators
    btn_click_admin_Xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
    btn_add_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    textbox_employee_name_xpath = "//*[@placeholder='Type for hints...']"
    link_user_role_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div"
    link_user_role_xpath_role_option_xpath = "//*[@role='option'][2]"
    link_status_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div"
    link_status_option_xpath = "//*[@role='option'][2]"
    text_admin_name_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input"
    textbox_user_password_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"
    textbox_confirm_password_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input"
    btn_save_xpath = "//*[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def click_admin(self):
        self.driver.find_element(By.XPATH, self.btn_click_admin_Xpath).click()


    def click_add(self):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()
        time.sleep(1)

    def enter_employee_name(self, name):
        field = self.driver.find_element(By.XPATH, self.textbox_employee_name_xpath)
        field.send_keys(name)
        time.sleep(2)
        field.click()

    def select_user_role(self, role="Admin"):
        self.driver.find_element(By.XPATH, self.link_user_role_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.link_user_role_xpath_role_option_xpath).click()

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.text_admin_name_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_user_password_xpath).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.textbox_confirm_password_xpath).send_keys(confirm_password)

    def set_status(self, status="Enabled"):
        self.driver.find_element(By.XPATH, self.link_status_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.link_status_option_xpath).click()

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
        time.sleep(2)




