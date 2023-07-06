from selenium.webdriver.common.by import By
from common import CommonOps


class SidingPage(CommonOps):

    ZIP_FIELD = (By.CSS_SELECTOR, "[data-autotest-input-0]")
    GET_ESTIMATE_BUTTON = (By.XPATH, "//button[@data-autotest-button-submit-0]")
    PROJECT_TYPE_1 = (By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-1]~label")
    PROJECT_TYPE_2 = (By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-2]~label")
    PROJECT_TYPE_3 = (By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-3]~label")
    PROJECT_TYPE_4 = (By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-4]~label")
    PROJECT_TYPE_5 = (By.CSS_SELECTOR, "[data-autotest-radio-sdprojecttype-5]~label")
    NEXT_BUTTON = (By.CSS_SELECTOR, "[data-autotest-button-submit-next]")
    SDKIND_1 = (By.CSS_SELECTOR, "[data-autotest-radio-sdkind-1]~label")
    SDKIND_2 = (By.CSS_SELECTOR, "[data-autotest-radio-sdkind-2]~label")
    SDKIND_3 = (By.CSS_SELECTOR, "[data-autotest-radio-sdkind-3]~label")
    SDKIND_4 = (By.CSS_SELECTOR, "[data-autotest-radio-sdkind-4]~label")
    SDKIND_5 = (By.CSS_SELECTOR, "[data-autotest-radio-sdkind-5]~label")
    AREA_FIELD = (By.CSS_SELECTOR, "[data-autotest-input-squarefeet-tel]")
    AREA_CHECKBOX = (By.CSS_SELECTOR, "[data-autotest-checkbox-notsure-]")
    STORIES_1 = (By.CSS_SELECTOR, "[data-autotest-radio-sdstories-1]~label")
    STORIES_2 = (By.CSS_SELECTOR, "[data-autotest-radio-sdstories-2]~label")
    STORIES_3 = (By.CSS_SELECTOR, "[data-autotest-radio-sdstories-3]~label")
    STORIES_4 = (By.CSS_SELECTOR, "[data-autotest-radio-sdstories-4]~label")
    OWNER_YES = (By.CSS_SELECTOR, "[data-autotest-radio-internalowner-1]~label")
    OWNER_NO = (By.CSS_SELECTOR, "[data-autotest-radio-internalowner-0]~label")
    NAME_FIELD = (By.CSS_SELECTOR, "[data-autotest-input-fullname-text]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[data-autotest-input-email-email]")
    PHONE_FIELD = (By.CSS_SELECTOR, "[data-autotest-input-phonenumber-tel]")
    SUBMIT_REQUEST_BUTTON = (By.CSS_SELECTOR, "[data-autotest-button-submit-submit-my-request]")
    EDIT_BUTTON = (By.CSS_SELECTOR, "[data-autotest-button-button-edit-phone-number]")
    CORRECT_BUTTON = (By.CSS_SELECTOR, "[data-autotest-button-submit-phone-number-is-correct]")
    THANK_YOU_BLOCK = (By.XPATH, "//div[@id='StepBodyId']/div/div/h4")

    def enter_zip_code(self, zip_code):
        self.find(self.ZIP_FIELD).send_keys(zip_code)

    def send_estimate(self):
        self.find(self.GET_ESTIMATE_BUTTON).click()

    def project_type(self, proj_type):
        if proj_type == 1:
            self.wait_for(self.PROJECT_TYPE_1).click()
        elif proj_type == 2:
            self.wait_for(self.PROJECT_TYPE_2).click()
        elif proj_type == 3:
            self.wait_for(self.PROJECT_TYPE_3).click()
        elif proj_type == 4:
            self.wait_for(self.PROJECT_TYPE_4).click()
        elif proj_type == 5:
            self.wait_for(self.PROJECT_TYPE_5).click()

    def next_button(self):
        self.find(self.NEXT_BUTTON).click()

    def select_sdkind(self, sdkind):
        if sdkind == 1:
            self.wait_for(self.SDKIND_1).click()
        elif sdkind == 2:
            self.wait_for(self.SDKIND_2).click()
        elif sdkind == 3:
            self.wait_for(self.SDKIND_3).click()
        elif sdkind == 4:
            self.wait_for(self.SDKIND_4).click()
        elif sdkind == 5:
            self.wait_for(self.SDKIND_5).click()

    def input_area_field(self, area):
        self.wait_for(self.AREA_FIELD).send_keys(area)

    def area_checkbox(self):
        self.find(self.AREA_CHECKBOX).click()

    def select_stories(self, stories):
        if stories == 1:
            self.wait_for(self.STORIES_1).click()
        elif stories == 2:
            self.wait_for(self.STORIES_2).click()
        elif stories == 3:
            self.wait_for(self.STORIES_3).click()
        elif stories == 4:
            self.wait_for(self.STORIES_4).click()

    def select_owner(self, option):
        if option == 'yes':
            self.wait_for(self.OWNER_YES).click()
        elif option == 'no':
            self.wait_for(self.OWNER_NO).click()

    def input_name(self, name):
        self.wait_for(self.NAME_FIELD).send_keys(name)

    def input_email(self, email):
        self.find(self.EMAIL_FIELD).send_keys(email)

    def input_phone(self, phone):
        self.wait_for(self.PHONE_FIELD).send_keys(phone)

    def submit_request_button(self):
        self.find(self.SUBMIT_REQUEST_BUTTON).click()

    def edit_button(self):
        self.wait_for(self.EDIT_BUTTON).click()

    def correct_button(self):
        self.wait_for(self.CORRECT_BUTTON).click()

    def last_page(self):
        return self.wait_for(self.THANK_YOU_BLOCK).text
