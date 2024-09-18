from playwright.sync_api import sync_playwright

class PlaywrightScraper:
    def __init__(self, url, headless=True):
        self.url = url
        self.headless = headless

    def fetch_content(self):
        """同步爬取整個頁面的 HTML 內容"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            page.goto(self.url)
            content = page.content()
            browser.close()
        return content

    def fetch_elements(self, selector):
        """同步爬取頁面，並根據選擇器返回所有匹配的元素文本和屬性"""
        processed_data = self._try_fetch_elements(selector)

        # 如果第一次爬取結果為空，嘗試重新設置 headless 為 False 再次爬取
        if not processed_data:
            print("未找到資料，嘗試以 headless=False 再次執行爬取...")
            self.headless = False
            processed_data = self._try_fetch_elements(selector)

        return processed_data

    def _try_fetch_elements(self, selector):
        """實際執行爬取邏輯"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            page.goto(self.url)

            processed_data = self._extract_data(page, selector)
            browser.close()

        return processed_data

    def _extract_data(self, page, selector):
        # 這個方法應該被子類重寫以適應特定網站的爬蟲邏輯
        raise NotImplementedError("子類必須實現 _extract_data 方法")

    def take_screenshot(self, path="screenshot.png"):
        """截取當前頁面的截圖，並保存到指定路徑"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            page.goto(self.url)
            page.screenshot(path=path)
            browser.close()

class BinanceScraper(PlaywrightScraper):
    def __init__(self):
        super().__init__('https://www.binance.com/zh-TC/support/announcement/%E6%95%B8%E5%AD%97%E8%B2%A8%E5%B9%A3%E5%8F%8A%E4%BA%A4%E6%98%93%E5%B0%8D%E4%B8%8A%E6%96%B0?c=48&navId=48&hl=zh-TC')

    def _extract_data(self, page, selector):
        links = page.query_selector_all(selector)
        processed_data = []
        for link in links:
            title_element = link.query_selector('div.css-1yxx6id')
            href = link.get_attribute('href')
            if title_element and href:
                title = title_element.inner_text()
                full_url = f"https://www.binance.com{href}"
                processed_data.append({
                    'title': title,
                    'url': full_url
                })
        return processed_data

class BingxScraper(PlaywrightScraper):
    def __init__(self):
        super().__init__('https://bingx.com/zh-cn/support/announcements/')

    def _extract_data(self, page, selector):
        articles = page.query_selector_all(selector)
        processed_data = []
        for article in articles:
            title_element = article.query_selector('h2')
            link_element = article.query_selector('a')
            if title_element and link_element:
                title = title_element.inner_text()
                href = link_element.get_attribute('href')
                full_url = f"https://bingx.com{href}"
                processed_data.append({
                    'title': title,
                    'url': full_url
                })
        return processed_data

class HashkeyScraper(PlaywrightScraper):
    def __init__(self):
        super().__init__('https://www.hashkey.com/zh-CN/support/announcements')

    def _extract_data(self, page, selector):
        items = page.query_selector_all(selector)
        processed_data = []
        for item in items:
            title_element = item.query_selector('.announcement-item-title')
            link_element = item.query_selector('a')
            if title_element and link_element:
                title = title_element.inner_text()
                href = link_element.get_attribute('href')
                full_url = f"https://www.hashkey.com{href}"
                processed_data.append({
                    'title': title,
                    'url': full_url
                })
        return processed_data

class OKXScraper(PlaywrightScraper):
    def __init__(self):
        super().__init__('https://www.okx.com/cn/help-center/section/announcements')

    def _extract_data(self, page, selector):
        items = page.query_selector_all(selector)
        processed_data = []
        for item in items:
            title_element = item.query_selector('.article-list-item-title')
            link_element = item
            if title_element and link_element:
                title = title_element.inner_text()
                href = link_element.get_attribute('href')
                full_url = f"https://www.okx.com{href}"
                processed_data.append({
                    'title': title,
                    'url': full_url
                })
        return processed_data

# 其他交易所的爬蟲類可以類似實現
