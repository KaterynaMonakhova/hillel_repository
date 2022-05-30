import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          options=options)

URL = ["https://www.aqa.science/admin"]


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def create_user_creds():
    users = {"login": "", "password": ""}
    for i in users:
        users[i] = generate_random_string(10)
    return users


def login_as_admin():
    admin_login = "admin"
    admin_password = "admin123"
    driver.get(URL[0])
    driver.find_element(by=By.XPATH, value='//*[@id="id_username"]').send_keys(admin_login)
    driver.find_element(by=By.XPATH, value='//*[@id="id_password"]').send_keys(admin_password)
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="login-form"]/div[3]/input')
    submit_button.click()
    assert driver.current_url == 'https://www.aqa.science/admin/'


def create_user():
    user = create_user_creds()
    login = user.get("login")
    password = user.get("password")
    driver.find_element(by=By.XPATH, value='//*[@id="content-main"]/div/table/tbody/tr[2]/td[1]/a').click()
    driver.find_element(by=By.XPATH, value='// *[ @ id = "id_username"]').send_keys(login)
    driver.find_element(by=By.XPATH, value='//*[@id="id_password1"]').send_keys(password)
    driver.find_element(by=By.XPATH, value='//*[@id="id_password2"]').send_keys(password)
    save_button = driver.find_element(by=By.CSS_SELECTOR, value='#user_form > div > div > input.default')
    save_button.click()
    assert "was added successfully" in driver.page_source, "User is not created successfully"
    assert driver.find_element(By.PARTIAL_LINK_TEXT, login), "Link not found"
    return user


def check_user():
    user = create_user()
    driver.find_element(by=By.XPATH, value='//*[@id="nav-sidebar"]/div/table/tbody/tr[2]/th/a').click()

    login = user.get("login")
    assert login in driver.page_source, "User does not exist"
    driver.find_element(by=By.LINK_TEXT, value=login).click()
    user_check = driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
    assert user_check == login, 'Username error'


def update_user():
    user = create_user()
    driver.find_element(by=By.XPATH, value='//*[@id="nav-sidebar"]/div/table/tbody/tr[2]/th/a').click()
    login = user.get("login")
    assert login in driver.page_source, "User does not exist"
    driver.find_element(by=By.LINK_TEXT, value=login).click()
    driver.find_element(by=By.XPATH, value='//*[@id="id_email"]').send_keys(f"{login}@gmail.com")
    save_changes_button = driver.find_element(by=By.CSS_SELECTOR, value='#user_form > div > div > input.default')
    save_changes_button.click()
    assert "was changed successfully" in driver.page_source, "User is not updated successfully"


def delete_user():
    user = create_user()
    driver.find_element(by=By.XPATH, value='//*[@id="nav-sidebar"]/div/table/tbody/tr[2]/th/a').click()
    login = user.get("login")
    assert login in driver.page_source, "User does not exist"
    driver.find_element(by=By.LINK_TEXT, value=login).click()
    driver.find_element(by=By.XPATH, value='//*[@id="id_email"]').send_keys(f"{login}@gmail.com")
    delete_button = driver.find_element(by=By.CSS_SELECTOR, value='#user_form > div > div > p > a')
    delete_button.click()
    accept_button = driver.find_element(by=By.CSS_SELECTOR,
                                        value='#content > form > div > input[type=submit]:nth-child(2)')
    accept_button.click()
    assert "was deleted successfully" in driver.page_source, "User is not deleted successfully"
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, login)
    except NoSuchElementException:
        return False
    return True


def test_create_user():
    login_as_admin()
    create_user()


def test_read_user():
    login_as_admin()
    check_user()


def test_update_user():
    login_as_admin()
    update_user()


def test_delete_user():
    login_as_admin()
    delete_user()
