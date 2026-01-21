from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PIMListPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.menu_pim = (By.XPATH, "//span[text()='PIM']")
        self.search_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "(//button[normalize-space()='Search'])[1]")
        self.table_rows = (By.XPATH, "//div[@class='oxd-table-body']/div")
        self.edit_button = (
            By.XPATH,
            "//div[@class='oxd-table-body']/div[1]//i[contains(@class,'bi-pencil')]/ancestor::button",
        )
        self.delete_button = (
            By.XPATH,
            "//i[contains(@class,'bi-trash')]/ancestor::button",
        )
        self.confirm_delete_button = (
            By.XPATH,
            "//button[contains(text(),'Yes, Delete')]",
        )
        self.NO_RECORD_MSG = (By.XPATH, "//span[text()='No Records Found']")

    
    
    def open(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_pim)).click()

    def search_employee(self, keyword):
        self.wait.until(EC.visibility_of_element_located(self.search_input)).clear()
        self.driver.find_element(*self.search_input).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def get_first_row_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.table_rows)).text

    def open_first_employee_detail(self):
        self.wait.until(EC.element_to_be_clickable(self.edit_button)).click()

    def delete_first_result(self):
        self.wait.until(EC.element_to_be_clickable(self.delete_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.confirm_delete_button)).click()

    def scroll_to_first_row(self):
        row = self.wait.until(EC.visibility_of_element_located(self.table_rows))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", row
        )

    def get_row_by_keyword(self, keyword):
        self.wait.until(EC.visibility_of_element_located(self.table_rows))
        rows = self.driver.find_elements(*self.table_rows)
        for row in rows:
            if keyword in row.text:
                return row
        return None

    def delete_row(self, row):
        # scroll ke row biar keliatan
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", row
        )

        # tombol delete di DALAM row
        delete_btn = row.find_element(
            By.XPATH, ".//i[contains(@class,'bi-trash')]/ancestor::button"
        )
        delete_btn.click()

        # tunggu modal confirm muncul
        confirm_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Yes, Delete']")
            )
        )
        confirm_btn.click()

    def get_no_record_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NO_RECORD_MSG)
        ).text