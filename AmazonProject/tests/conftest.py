import pytest
from selenium import webdriver


#browser invocation
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    # implicit timing
    driver.implicitly_wait(12)
    driver.get(
        "https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
