from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):

        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon).to_be_visible()

        no_result_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_result_text).to_be_visible()
        expect(no_result_text).to_have_text('There is no results')

        no_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(no_description_text).to_be_visible()
        expect(no_description_text).to_have_text('Results from the load test pipeline will be displayed here')

        chromium_page_with_state.wait_for_timeout(5000)
