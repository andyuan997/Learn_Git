from playwright.sync_api import sync_playwright

def scrape_titles_and_links():
    with sync_playwright() as p:
        # 启动浏览器，设置 headless=False 以查看浏览器行为
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 打开目标页面
        page.goto("https://bingx.com/zh-tw/support/notice-center/")

        # 等待页面加载完成
        page.wait_for_load_state('networkidle')

        # 给页面更多时间加载内容
        #page.wait_for_timeout(5000)  # 等待 5 秒，确保动态内容加载完毕

        # 查找新闻标题和链接的元素
        news_items = page.query_selector_all('a[data-v-1ffda950]')

        if news_items:
            for item in news_items:
                title = item.query_selector('.article-title').inner_text().strip()
                link = item.get_attribute('href')
                full_link = f"https://bingx.com{link}"  # 拼接完整链接
                print(f"标题: {title}, 链接: {full_link}")
        else:
            print("未找到新闻项目")

        # 关闭浏览器
        browser.close()

# 运行爬虫
scrape_titles_and_links()
