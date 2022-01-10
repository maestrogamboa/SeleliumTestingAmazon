from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
### Pytest HTMl Report ###

def pytest_configure(config):
    config._metadata['Project Name'] = 'Amazon Test'
    config._metadata['Module Name'] = 'Loging'
    config._metadata['Tester'] = 'Edgard'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
