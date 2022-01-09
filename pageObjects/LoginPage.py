class LoginPage:
    text_username_xpath = "//input[@id='ap_email']"
    continue_button_xpath = "//input[@id='continue']"
    textbox_password_xpath = "//input[@id='ap_password']"
    button_login_xpath = "//input[@id='signInSubmit']"
    logout_menu_xpath = "//span[normalize-space()='Account & Lists']"

    def __init__(self, driver):
        self.driver = driver
    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.text_username_xpath).clear()
        self.driver.find_element_by_xpath(self.text_username_xpath).send_keys(username)
    def clickContinue(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()
    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()


