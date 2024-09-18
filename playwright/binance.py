from playwright.sync_api import sync_playwright


def fetch_binance_titles_and_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # 打開碧安公告頁面
        page.goto(
            'https://www.binance.com/zh-TC/support/announcement/%E6%95%B8%E5%AD%97%E8%B2%A8%E5%B9%A3%E5%8F%8A%E4%BA%A4%E6%98%93%E5%B0%8D%E4%B8%8A%E6%96%B0?c=48&navId=48&hl=zh-TC')

        # 抓取所有公告的 <a> 標籤，其中包含標題和連結
        links = page.query_selector_all('a.css-1w8j6ia')

        # 打印每個標題和連結
        for link in links:
            title = link.query_selector('div.css-1yxx6id').inner_text()
            href = link.get_attribute('href')
            full_url = f"https://www.binance.com{href}"  # 拼接完整的URL
            print(f"標題: {title}")
            print(f"連結: {full_url}\n")

        browser.close()


if __name__ == "__main__":
    fetch_binance_titles_and_links()
