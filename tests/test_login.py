from pages.login_page import LoginPage
from utils.data_loader import load_json_data

def test_valid_login(page_fixture):
    # 1. Load data from JSON
    data = load_json_data()
    
    # 2. Perform actions using the JSON data
    login = LoginPage(page_fixture)
    login.do_login(data["username"], data["password"])
    
    assert "inventory" in page_fixture.url