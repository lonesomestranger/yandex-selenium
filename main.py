import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def create_custom_driver(driver_path, yandex_browser_path, headless=False):
    options = Options()

    if headless:
        options.add_argument("--headless")

    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    options.binary_location = yandex_browser_path

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

if __name__ == "__main__":
    driver_path = 'yandexdriver.exe' # path to your yandexdriver

    yandex_browser_path = r"C:\Users\User\AppData\Local\Yandex\YandexBrowser\Application\browser.exe" # or another path to Yandex.Browser core

    driver = create_custom_driver(driver_path, yandex_browser_path, headless=False)

    driver.get('https://yandex.ru')
    time.sleep(10)
    driver.quit()
    