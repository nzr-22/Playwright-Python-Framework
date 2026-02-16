import pytest
from utils.data_loader import load_json_data

# The "page" argument here comes from the Playwright plugin automatically
@pytest.fixture(scope="function")
def page_fixture(page):
    
    # 1. Load data using your existing utility
    data = load_json_data()
    
    # 2. Go to the URL from the JSON file
    page.goto(data["url"])
    
    # 3. Give the page to the test
    yield page