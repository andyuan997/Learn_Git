from factories import AnnouncementScraperFactory


def main():
    # 直接根據網站名稱調用不同的爬蟲邏輯
    website_name = "Binance"  # 或 "OKX"
    factory = AnnouncementScraperFactory(website_name)

    # 根據網站名稱抓取並處理公告數據
    processed_data = factory.get_scraper_and_process()

    # 打印結果
    for data in processed_data:
        print(f"標題: {data['title']}")
        print(f"連結: {data['url']}\n")

if __name__ == "__main__":
    main()
