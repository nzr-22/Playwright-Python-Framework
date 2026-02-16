from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_json_data

def test_add_item_to_cart(page_fixture):
    # 1. Load data from JSON
    data = load_json_data()
    
    # 2. Login Logic (Reused)
    login = LoginPage(page_fixture)
    login.do_login(data["username"], data["password"])

    # 3. Inventory Logic
    inventory = InventoryPage(page_fixture)
    inventory.add_backpack_to_cart()

    # 4. Assertion
    # We verify the cart count changed to '1'
    count = inventory.get_cart_count()
    assert count == "1", f"Expected 1 item in cart but found {count}"