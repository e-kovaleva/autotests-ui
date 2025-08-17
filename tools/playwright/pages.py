import allure
from typing import Generator
from playwright.sync_api import Page, Playwright
from config import Browser, settings
from pathlib import Path


def initialize_playwright_page(
        playwright: Playwright, test_name: str, browser_type: Browser, storage_state: Path | None = None
    ) -> Generator[Page, None, None]:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(), storage_state=storage_state, record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()

    allure.attach.file(
        source=settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip'
    )
    if page.video:
        allure.attach.file(
            source=page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM
        )
