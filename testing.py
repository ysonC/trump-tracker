from playwright.sync_api import sync_playwright

TRUMP_URL = "https://truthsocial.com/@realDonaldTrump"


def get_posts(number):
    scrapped_post = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(TRUMP_URL)

        page.wait_for_timeout(2000)
        containers = page.locator("div.status__content-wrapper p.text-base")
        print(containers.first.inner_text())
        containers = page.locator("div.status__content-wrapper")
        print(containers.first.inner_text())

        browser.close()
        return scrapped_post


if __name__ == "__main__":
    truth = get_posts(30)
    print(truth)
