from selenium import webdriver
from selenium.webdriver.edge.options import Options

def get_driver(browser="chrome"):
    browser = browser.lower()

    if browser == "edge":
        options = Options()
        options.page_load_strategy = "eager"   # 🔥 penting
        driver = webdriver.Edge(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    return driver
