import requests

class DiscordNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_notification(self, message):
        """發送 Discord 通知"""
        data = {"content": message}
        response = requests.post(self.webhook_url, json=data)

        if response.status_code == 204:
            print("通知發送成功")
        else:
            print(f"通知發送失敗: {response.status_code}")

# 使用示例
if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/your_webhook_url"
    notifier = DiscordNotifier(webhook_url)
    notifier.send_notification("這是一條測試通知，來自你的爬蟲系統")
