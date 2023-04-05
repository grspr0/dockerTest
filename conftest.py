import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def browser(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.set_capability("loggingPrefs", {'performance': 'ALL'})
    service = ChromeService()
    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.set_window_size(1920, 1080)
    size = driver.get_window_size()
    print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))
    yield driver
    driver.quit()


