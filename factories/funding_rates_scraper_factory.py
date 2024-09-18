from scrapers.api_scraper import APIScraper


class FundingRatesScraperFactory:
    """
    處理資費數據爬取，根據不同交易所使用不同的 API。
    """

    def __init__(self, website_info):
        self.website_info = website_info

    def get_scrapers(self):
        scrapers = []
        if "api" in self.website_info["types"]:
            api_url = self.website_info.get("api_url")
            if api_url:
                scrapers.append(APIScraper(api_url))
            else:
                raise ValueError("API URL 未找到")

        if not scrapers:
            raise ValueError(f"無法找到爬取方式: {self.website_info['types']}")

        return scrapers
