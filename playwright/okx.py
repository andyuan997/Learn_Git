from playwright.sync_api import sync_playwright


def fetch_okx_titles_and_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # 打開目標頁面
        page.goto('https://www.okx.com/zh-hant/help/section/announcements-latest-announcements')

        # 抓取所有公告的 <a> 標籤，其中包含標題和連結
        links = page.query_selector_all('a.okui-powerLink.index_articleItem__d-8iK')

        # 打印每個標題和連結
        for link in links:
            title = link.query_selector('div.index_title__iTmos.index_articleTitle__ys7G7').inner_text()
            href = link.get_attribute('href')
            full_url = f"https://www.okx.com{href}"  # 拼接完整的URL
            print(f"標題: {title}")
            print(f"連結: {full_url}\n")

        browser.close()


if __name__ == "__main__":
    fetch_okx_titles_and_links()
