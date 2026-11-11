from playwright.sync_api import sync_playwright

def get_variable_from_running_browser(variable_name):
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = context.pages[0]  # or find the right tab by URL

        value = page.evaluate(f"window.{variable_name}")
        return value