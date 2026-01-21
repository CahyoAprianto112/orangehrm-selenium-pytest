from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PIMAddPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # locators
        self.menu_pim = (By.XPATH, "//span[text()='PIM']")
        self.add_button = (By.XPATH, "(//button[normalize-space()='Add'])[1]")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.employee_id_input = (
            By.XPATH,
            "//label[text()='Employee Id']/../following-sibling::div/input",
        )
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.form_loader = (By.XPATH, "//div[contains(@class,'oxd-form-loader')]")
        self.required_error = (By.XPATH, "//span[text()='Required']")

    def click_save_without_input(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def open_add_employee_form(self):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

    
    def get_required_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.required_error)
        ).text
        
    def navigate_to_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_pim)).click()

    def add_employee(self, first_name, last_name, employee_id):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()
        self.wait.until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        emp_id = self.driver.find_element(*self.employee_id_input)
        emp_id.clear()
        emp_id.send_keys(employee_id)
        # ⏳ TUNGGU LOADER HILANG
        self.wait.until(EC.invisibility_of_element_located(self.form_loader))
        save_btn = self.wait.until(EC.element_to_be_clickable(self.save_button))
        # scroll biar aman
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", save_btn
        )
        # klik pake JS (anti ketahan overlay)
        self.driver.execute_script("arguments[0].click();", save_btn)
