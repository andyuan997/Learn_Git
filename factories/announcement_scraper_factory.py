from scrapers.playwright_scraper import BinanceScraper, BingxScraper, HashkeyScraper, OKXScraper

class AnnouncementScraperFactory:
    @staticmethod
    def create_scraper(exchange):
        if exchange.lower() == 'binance':
            return BinanceScraper()
        elif exchange.lower() == 'bingx':
            return BingxScraper()
        elif exchange.lower() == 'hashkey':
            return HashkeyScraper()
        elif exchange.lower() == 'okx':
            return OKXScraper()
        else:
            raise ValueError(f"不支持的交易所: {exchange}")

def test_scrapers():
    exchanges = ["binance", "bingx", "hashkey", "okx"]

    for exchange in exchanges:
        print(f"\n爬取 {exchange.upper()} 的公告:")
        try:
            scraper = AnnouncementScraperFactory.create_scraper(exchange)
            data = scraper.fetch_elements()
            
            if not data:
                print(f"警告：{exchange} 沒有找到任何公告。")
                continue

            for item in data[:3]:  # 只打印前3條公告
                print(f"標題: {item['title']}")
                print(f"連結: {item['url']}")
                print()

        except Exception as e:
            print(f"錯誤：爬取 {exchange} 時發生異常 - {str(e)}")

    print("\n測試完成。")

if __name__ == "__main__":
    test_scrapers()
