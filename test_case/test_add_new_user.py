
from selenium.webdriver.common.by import By
from base_page.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from time import sleep
from base_page.add_customer_page import add_customer_page


class Test_02_Add_New_user:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_password = Read_Config.get_invalid_password()

    def test_add_new_user(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)

        # Login to Admin
        self.login_admin = Login_Admin_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.password)
        self.login_admin.click_login()

        self.driver.implicitly_wait(5)
        act_dashboard_text = self.driver.find_element(By.XPATH, "//h6[contains(.,'Dashboard')]").text

        if act_dashboard_text == "Dashboard":
            # Proceed with Add User steps
            self.add_user = add_customer_page(self.driver)
            self.add_user.click_admin()
            self.add_user.click_add()
            self.add_user.enter_employee_name("John Smith")
            self.add_user.select_user_role("Admin")
            self.add_user.enter_username("john.smith")
            self.add_user.enter_password("StrongPass123")
            self.add_user.enter_confirm_password("StrongPass123")
            self.add_user.set_status("Enabled")
            self.add_user.click_save()

            # Optional: Assert some success message or redirection here
            assert True
        else:
            sleep(5)
            self.driver.save_screenshot(".\\screenshots\\test_Valid_Login_Verification.png")
            assert False

        self.driver.close()

    def test_Invalid_Login_Verification(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.login_admin = Login_Admin_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.invalid_password)
        self.login_admin.click_login()

        self.driver.implicitly_wait(5)
        act_dashboard_text = self.driver.find_element(By.XPATH, "//p[contains(.,'Invalid credentials')]").text

        if act_dashboard_text == "Invalid credentials":
            assert True
        else:
            sleep(5)
            self.driver.save_screenshot(".\\screenshots\\test_Invalid_Login_Verification.png")
            assert False

        self.driver.close()
