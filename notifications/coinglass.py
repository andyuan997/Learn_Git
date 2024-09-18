from playwright.sync_api import sync_playwright

def fetch_all_symbol_names():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # 打開目標頁面
        page.goto('https://www.coinglass.com/zh-TW/FrArbitrage')
        # 抓取所有 class 為 "symbol-name" 的元素
        symbol_names = page.query_selector_all('.symbol-name')
        # 打印每個匹配到的元素的文本
        for symbol in symbol_names:
            print(symbol.inner_text())
        browser.close()

if __name__ == "__main__":
    fetch_all_symbol_names()