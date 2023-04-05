from helpers.BasePageHelpers import BasePageHelpers
from locators.BasePageLocators import BasePageLocators


def test__check_links(browser):
    assert_links_method = BasePageHelpers(browser)
    assert_links_method.find_link(BasePageLocators.muscle_booster_link, 'Muscle Booster')
    assert_links_method.find_link(BasePageLocators.fitcoach_link, 'FitCoach')
    assert_links_method.find_link(BasePageLocators.yoga_link, 'Yoga-Go')
    assert_links_method.find_link(BasePageLocators.omo_link, 'Omo')

