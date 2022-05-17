"""
prerequisites  = https://www.ukr.net/
1. Open the URL.
2. Click the "Sinoptik" link.
3. Go to the open tab.
4. Fill the "Київ" to the search field.
5. Check the element is "Столиця України"
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          options=options)


city_name = "Київ"


url = ["https://www.ukr.net/"]

driver.get(url[0])
driver.find_element(by=By.LINK_TEXT, value='Sinoptik').click()
driver.switch_to.window(window_name=driver.window_handles[-1])
wait = WebDriverWait(driver, 5)
search_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search_city"]')))
search_field.send_keys(city_name)
button = '/html/body/div[4]/div[1]/form/p[1]/input[2]'
element_button = driver.find_element(By.XPATH, button)
element_button.click()

expected_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[4]/div')))
print(expected_element.text)
if expected_element.text == "Столиця України":
    print("Successful")
else:
    print("Failed")



