class LoginPage:
    
    # Constructor: receives the 'page' from the test
    def __init__(self, page):
        self.page = page
        # Locators (Stored as strings)
        self._username_box = "#user-name"  # CSS Selector for ID
        self._password_box = "#password"
        self._login_btn    = "#login-button"

    # Actions
    def enter_username(self, user):
        self.page.fill(self._username_box, user)

    def enter_password(self, password):
        self.page.fill(self._password_box, password)

    def click_login(self):
        self.page.click(self._login_btn)

    # Combined Action
    def do_login(self, user, password):
        self.enter_username(user)
        self.enter_password(password)
        self.click_login()