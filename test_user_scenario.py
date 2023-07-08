import random
import time

from pages.siding_page import SidingPage


def test_user_scenario_one(driver):
    side = SidingPage(driver)

    assert side.check_start_page_header() == "How Much Does Siding Cost In Your Location?"
    # assert side.find_location() == "The Phnom Penh, 12 Area"  # depends on run test location, but don't work now
    side.enter_zip_code('09090')

    assert side.check_right_icon()
    side.send_estimate()
    time.sleep(3)

    assert side.check_page_header() == "What type of project is this?"
    side.project_type(1)
    side.next_button()
    time.sleep(3)

    assert side.check_page_header() == "What kind of siding do you want?"
    side.select_sdkind(1)
    side.next_button()
    time.sleep(3)

    assert side.check_page_header() == "Approximately how many square feet will be covered with new siding?"
    side.input_area_field(1000)
    side.next_button()
    time.sleep(3)

    assert side.check_page_header() == "How many stories is your house?"
    side.select_stories(1)
    side.next_button()
    time.sleep(3)

    assert side.check_page_header() == "Are you the homeowner or authorized to make property changes?"
    side.select_owner('yes')
    side.next_button()
    time.sleep(3)

    assert side.check_page_header() == "Who should I prepare this estimate for?"
    side.input_name('Testname Check')
    side.input_email(f'test_check{random.randint(1, 1000)}@gmail.com')
    side.next_button()
    time.sleep(3)

    assert side.check_page_header() == "What is your phone number?"
    side.input_phone(random.randint(1000000000, 9999999999))
    side.submit_request_button()
    time.sleep(5)

    assert side.check_page_header() == "Please confirm your phone number."
    side.correct_button()
    time.sleep(5)
    assert side.check_page_header() == 'Thank you Testname, your contractor QA Customer will call soon!'





