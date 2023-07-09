import random
import time

import allure
from allure import step

from pages.siding_page import SidingPage
from helpers.find_my_location import get_location


@allure.label("owner", "Interviewee Artem")
@allure.story("Choose siding scenario")
@allure.feature("Find user location")
def test_check_find_user_location(driver):
    side = SidingPage(driver)

    with step("Check find client location is correct"):
        client_location = get_location()
        assert side.find_location() == f"The {client_location} Area"


@allure.label("owner", "Interviewee Artem")
@allure.story("Choose siding scenario")
@allure.feature("Try send form without zip code")
def test_send_estimate_without_zipcode(driver):
    side = SidingPage(driver)

    with step("Send estimate without zipcode"):
        assert side.right_icon()
        side.send_estimate()
        assert side.enter_zipcode_warn() == "Enter your ZIP Code"


@allure.label("owner", "Interviewee Artem")
@allure.story("Choose siding scenario")
@allure.feature("Filling form with zip code without contractors")
def test_no_match_contractors_in_area(driver):
    side = SidingPage(driver)

    with step("Send zipcode area with no contractors"):
        side.enter_zip_code("00000")
        assert side.right_icon()
        side.send_estimate()
        assert side.page_header() == "Unfortunately, I have no matching contractors in your area yet."
    with step("Send email"):
        side.input_email("test_check1@gmail.com")
        side.submit_button()
    with step("Try another zip code and return to start page"):
        contact_message = "Thank you for your interest, we will contact you when " \
                          "our service becomes available in your area!"
        time.sleep(3)
        assert side.page_header() == contact_message
        side.try_another_zipcode_button()
    with step("Check answer on start page"):
        assert side.what_zip_code_answer() == "What is your ZIP Code?"


@allure.label("owner", "Interviewee Artem")
@allure.story("Choose siding scenario")
@allure.feature("Successful completion of the form, choosing first options")
def test_user_scenario_choose_first_options(driver):
    side = SidingPage(driver)

    with step("Check zip code and send"):
        side.enter_zip_code("09090")
        assert side.right_icon()
        side.send_estimate()
    with step("Choose project type"):
        assert side.is_button_enabled() is False, "Error: Button is clickable before option have chosen"
        side.project_type(1)
        side.next_button()
    with step("Choose side kind"):
        side.select_sdkind(1)
        side.next_button()
    with step("Choose area field"):
        side.input_area_field(1000)
        side.next_button()
    with step("Select stories"):
        side.select_stories(1)
        side.next_button()
    with step("Select owner"):
        side.select_owner("yes")
        side.next_button()
    with step("Input name and email"):
        side.input_name("Testname Check")
        side.input_email("test_check2@gmail.com")
        side.next_button()
    with step("Input phone"):
        side.input_phone(random.randint(1000000000, 9999999999))
        side.submit_request_button()
    with step("Phone number confirmation"):
        side.correct_button()
    with step("Check adding client name in text"):
        time.sleep(10)
        assert side.page_header() == "Thank you Testname, your contractor QA Customer will call soon!"


@allure.label("owner", "Interviewee Artem")
@allure.story("Choose siding scenario")
@allure.feature("Successful completion of the form, choosing 'not sure' options when it possible")
def test_user_scenario_not_sure_options(driver):
    side = SidingPage(driver)

    with step("Check zip code and send"):
        side.enter_zip_code("09090")
        assert side.right_icon()
        side.send_estimate()
    with step("Choose project type"):
        assert side.is_button_enabled() is False, "Error: Button is clickable before option have chosen"
        side.project_type(5)
        side.next_button()
    with step("Choose side kind"):
        side.select_sdkind(5)
        side.next_button()
    with step("Choose area field"):
        side.area_checkbox()
        side.next_button()
    with step("Select stories"):
        side.select_stories(2)
        side.next_button()
    with step("Select owner"):
        side.select_owner("no")
        alert = "Our contractors require the homeowner or someone authorized to make " \
                "property changes be present during the estimate. Would you like to continue?"
        assert side.owner_alert() == alert
        side.owner_continue("yes")
    with step("Input name and email"):
        side.input_name("Testname Check")
        side.input_email("test_check3@gmail.com")
        side.next_button()
    with step("Input phone"):
        side.input_phone(random.randint(1000000000, 9999999999))
        side.submit_request_button()
    with step("Phone number confirmation"):
        side.correct_button()
    with step("Check adding client name in text"):
        time.sleep(10)
        assert side.page_header() == "Thank you Testname, your contractor QA Customer will call soon!"
