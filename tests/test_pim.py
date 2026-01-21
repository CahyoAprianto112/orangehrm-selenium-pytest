import time

import pytest

from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage
from pages.pim_add_page import PIMAddPage
from pages.pim_list_page import PIMListPage


@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("cymera", "admin123")
    time.sleep(3)
    return driver


@pytest.mark.smoke
def test_add_employee(login):
    pim_list = PIMListPage(login)
    pim_add = PIMAddPage(login)
    personal = PersonalDetailsPage(login)

    pim_list.open()
    pim_add.add_employee("Cymera", "Okta", "123445")

    toast = personal.get_toast_message()
    assert "Success" in toast


@pytest.mark.smoke
def test_add_and_search_employee(login):
    pim_list = PIMListPage(login)
    pim_add = PIMAddPage(login)
    personal = PersonalDetailsPage(login)

    first_name = "Cymera"
    last_name = "Diana"
    emp_id = "12345"

    pim_list.open()
    pim_add.add_employee(first_name, last_name, emp_id)

    toast = personal.get_toast_message()
    assert "Success" in toast
    # balik ke list + search
    time.sleep(3)
    pim_list.open()
    pim_list.search_employee(first_name)
    pim_list.scroll_to_first_row()
    time.sleep(2)
    first_row = pim_list.get_first_row_text()
    assert first_name in first_row
    time.sleep(3)

def test_add_employee_required_field(login):
    pim_list = PIMListPage(login)
    pim_add = PIMAddPage(login)

    pim_list.open()
    pim_add.open_add_employee_form()
    pim_add.click_save_without_input()

    error = pim_add.get_required_error()
    assert "Required" in error


@pytest.mark.regression
def test_search_employee(login):
    pim_list = PIMListPage(login)

    first_name = "Cymera"

    pim_list.open()
    pim_list.search_employee(first_name)
    pim_list.scroll_to_first_row()
    time.sleep(2)
    first_row = pim_list.get_first_row_text()
    assert first_name in first_row
    time.sleep(2)

def test_search_employee_not_found(login):
    pim_list = PIMListPage(login)

    first_name = "NotFound"
    
    pim_list.open()
    pim_list.search_employee(first_name)

    msg = pim_list.get_no_record_message()
    assert "No Records Found" in msg
    time.sleep(2)


@pytest.mark.regression
def test_edit_employee(login):
    pim_list = PIMListPage(login)
    personal = PersonalDetailsPage(login)

    first_name = "Cymera"
    last_name = "Diana"
    new_last_name = "Lovely"

    # SEARCH
    pim_list.open()
    pim_list.search_employee(first_name + " " + last_name) 
    pim_list.scroll_to_first_row()
    pim_list.open_first_employee_detail()

    # EDIT
    personal.wait_until_loaded()
    personal.update_last_name(new_last_name)

    toast = personal.get_toast_message()
    assert "Successfully" in toast


@pytest.mark.smoke
def test_add_search_edit_employee(login):
    pim_list = PIMListPage(login)
    pim_add = PIMAddPage(login)
    personal = PersonalDetailsPage(login)

    first_name = "Cymera"
    last_name = "Fyona"
    new_last_name = "Cyntia"
    emp_id = "123459"

    # ADD
    pim_list.open()
    pim_add.add_employee(first_name, last_name, emp_id)

    toast = personal.get_toast_message()
    assert "Success" in toast

    # BALIK KE LIST (WAJIB)
    pim_list.open()

    # SEARCH
    pim_list.search_employee(first_name + " " + last_name)
    pim_list.scroll_to_first_row()
    pim_list.open_first_employee_detail()

    # EDIT
    personal.wait_until_loaded()
    personal.update_last_name(new_last_name)

    toast = personal.get_toast_message()
    assert "Successfully" in toast


@pytest.mark.regression
def test_search_and_delete_employee(login):
    pim_list = PIMListPage(login)
    personal = PersonalDetailsPage(login)

    emp_id = "046712345"
    pim_list.open()
    pim_list.search_employee(emp_id)

    row = pim_list.get_row_by_keyword(emp_id)
    assert row is not None, "Employee tidak ditemukan, batal delete"
    pim_list.delete_row(row)
    toast = personal.get_toast_message()
    assert "Success" in toast



