# Тест 1. Навигация и проверка URL
# Откройте страницу https://httpbin.qa-territory.online.
# Найдите и кликните на ссылку HTML Form.
# Проверьте, что URL изменился на /forms/post.
# Вернитесь назад на главную страницу.
# Проверьте, что вернулись на исходный URL.


from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    original_url = driver.current_url
    driver.maximize_window()
    # driver.find_element(By.CSS_SELECTOR,'[href="/forms/post"]').click()
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    current_url = driver.current_url
    assert current_url.endswith("/forms/post")
    driver.back()
    current_url = driver.current_url
    assert current_url == original_url
    driver.quit()

