BOT_TOKEN = "TOKEN"  # Token from botfather
SHOP_NAME = "Зеленопарк"
SPREADSHEET_NAME = "Тир зеленопарк"
SERVICE_ACCOUNT_FILE = "FILE_PATH"  # Json for autification in service account

WORKSHEET_INDEXES = {
    "arcade": 0,
    "main": 1,
    "stock": 2,
    "defective": 3,
    "misc": 4
}

JSON_PATHS = {
    "arcade": "arcade/arcade.json",
    "main": {
        "350": "main/350.json",
        "1000": "main/1000.json",
        "1500": "main/1500.json",
        "2000": "main/2000.json"
    },
    "stock": {
        "350": "stock/350.json",
        "1000": "stock/1000.json",
        "1500": "stock/1500.json",
        "2000": "stock/2000.json"
    },
    "defective": "defective/defective.json",
    "misc": "misc/misc.json"
}
