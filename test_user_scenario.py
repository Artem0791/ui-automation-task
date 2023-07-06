import random
import time

from pages.siding_page import SidingPage


def test_user_scenarios_one(driver):
    side = SidingPage(driver)

    side.enter_zip_code('09090')
    side.send_estimate()

    side.project_type(1)
    side.next_button()

    side.select_sdkind(1)
    side.next_button()

    side.input_area_field(1000)
    side.next_button()

    side.select_stories(1)
    side.next_button()

    side.select_owner('yes')
    side.next_button()

    side.input_name('Test Check')
    side.input_email(f'test_check{random.randint(1, 1000)}@gmail.com')
    side.next_button()

    side.input_phone(random.randint(1000000000, 9999999999))
    side.submit_request_button()
    time.sleep(5)
    side.correct_button()
    time.sleep(5)
    assert side.last_page() == 'Thank you Test, your contractor QA Customer will call soon!'





