import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    url = "https://hb-eta.stage.sirenltd.dev/siding"
    service = Service(os.getenv('PATH'))
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    yield driver
    driver.close()
