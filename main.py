from playwright.sync_api import sync_playwright

TRUMP_URL = "https://truthsocial.com/@realDonaldTrump"


def get_posts(number):
    scrapped_post = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(TRUMP_URL)

        page.wait_for_timeout(2000)
        for _ in range(number):
            page.wait_for_timeout(2000)
            posts = page.locator("div.status__content-wrapper p.text-base")
            for i in range(posts.count()):
                scrapped_post.append(posts.nth(i).inner_text())
            page.mouse.wheel(0, 1000)

        browser.close()
        return scrapped_post


if __name__ == "__main__":
    truth = get_posts(30)
    print(truth)
