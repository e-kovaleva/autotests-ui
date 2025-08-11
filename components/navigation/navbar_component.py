from playwright.sync_api import expect, Page
from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, locator='navigation-navbar-app-title-text', name='Title')
        self.welcome_title = Text(page, locator='navigation-navbar-welcome-title-text', name='Welcome')

    def check_visible(self, username: str):
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')
