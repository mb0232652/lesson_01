# Тест 3. Проверка нескольких элементов
# Откройте страницу https://httpbin.qa-territory.online/links/10.
# Найдите все ссылки на странице (тег <a>
# Проверьте, что количество ссылок равно 9.
# Проверьте, что все ссылки отображаются на странице.
# Проверьте, что текст первой ссылки содержит "1"

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    driver.maximize_window()

    links = driver.find_elements(By.TAG_NAME, 'a')
    assert len(links) == 9

    for link in links:
        assert link.is_displayed()

        assert "1" in links[0].text

    driver.quit()

