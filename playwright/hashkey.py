from playwright.sync_api import sync_playwright

def scrape_titles_and_links():
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=True)  # 如果想手动查看浏览器行为，可以将 headless=False
        page = browser.new_page()

        # 打开目标页面
        page.goto("https://support.global.hashkey.com/hc/zh-tw/sections/12949261970588-%E6%95%B8%E5%AD%97%E8%B2%A8%E5%B9%A3%E5%8F%8A%E4%BA%A4%E6%98%93%E5%B0%8D%E4%B8%8A%E6%96%B0")

        # 等待页面加载完成
        page.wait_for_load_state('networkidle')

        # 查找文章标题和链接的元素
        news_items = page.query_selector_all('a.article-list-link')

        if news_items:
            for item in news_items:
                title = item.inner_text().strip()  # 获取文章标题
                link = item.get_attribute('href')  # 获取相对链接
                full_link = f"https://support.global.hashkey.com{link}"  # 拼接完整链接
                print(f"标题: {title}, 链接: {full_link}")
        else:
            print("未找到新闻项目")

        # 关闭浏览器
        browser.close()

# 运行爬虫
scrape_titles_and_links()
