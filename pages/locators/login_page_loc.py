from selenium.webdriver.common.by import By


email = (By.ID, 'user-name')
password = (By.ID, 'password')
send_button = (By.CSS_SELECTOR, 'input[type="submit"]')
error_panel = (By.CSS_SELECTOR, 'h3[data-test="error"]')
