from playwright.sync_api import sync_playwright

def scrape_titles_and_links():
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 打开目标页面
        page.goto("https://foresightnews.pro/news")

        # 等待页面加载并抓取包含新闻标题和链接的元素
        news_items = page.query_selector_all('a.news_body_title')

        # 提取新闻标题和链接
        for item in news_items:
            title = item.inner_text()
            link = item.get_attribute('href')
            print(f"標題: {title}")
            print(f"連結: https://foresightnews.pro{link}\n")

        # 关闭浏览器
        browser.close()

# 运行爬虫
scrape_titles_and_links()
