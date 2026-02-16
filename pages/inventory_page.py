class InventoryPage:
    def __init__(self, page):
        self.page = page
        # Locators (Using Playwright's specific 'locator' syntax)
        self._backpack_add_btn = page.locator("#add-to-cart-sauce-labs-backpack")
        self._cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self):
        # Playwright automatically waits for the button to be clickable
        self._backpack_add_btn.click()

    def get_cart_count(self):
        # Returns the text (e.g., "1") from the red badge
        return self._cart_badge.inner_text()