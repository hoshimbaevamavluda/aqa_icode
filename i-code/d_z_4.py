import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("user_name", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
])
def test_for_all_users(user_name):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    time.sleep(1)
    username = driver.find_element(By.ID, "user-name")
    username.send_keys(user_name)
    time.sleep(1)
    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")
    time.sleep(1)
    login_btn = driver.find_element(By.CSS_SELECTOR, "input#login-button")
    login_btn.click()

    time.sleep(3)
    driver.quit()

