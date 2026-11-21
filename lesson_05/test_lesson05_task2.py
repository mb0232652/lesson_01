# Тест 2. Работа с текстовым полем и кнопкой

# Шаги:

# Откройте страницу https://httpbin.qa-territory.online/forms/post.
# Найдите поле ввода с названием custname.
# Введите в него ваше имя.
# Найдите кнопку Submit и нажмите на нее.
# Проверьте, что после нажатия URL изменился.

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    original_url = driver.current_url
    driver.maximize_window()

    iprut_custname = driver.find_element(By.ID, "custname")
    iprut_custname.send_keys("Например,Мария")

    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    current_url = driver.current_url
    assert current_url != original_url

    driver.quit()

