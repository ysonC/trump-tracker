import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

TRUMP_URL = "https://truthsocial.com/@realDonaldTrump"


def extract_from_html(html: str):
    soup = BeautifulSoup(html, "html.parser")
    posts = soup.select("div.break-words")
    return [post.get_text(strip=True) for post in posts if post]


def get_latest_post():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(TRUMP_URL)

        time.sleep(2)
        for _ in range(10):
            page.wait_for_timeout(2000)
            posts = page.locator("div.status.cursor-pointer.focusable p.text-base")
            for i in range(posts.count()):
                print(posts.nth(i).inner_text())
            page.mouse.wheel(0, 1000)

        # print(posts.all_inner_texts())
        html = page.content()
        browser.close()
        return extract_from_html(html)


if __name__ == "__main__":
    truth = get_latest_post()
