import gspread
from config import SPREADSHEET_NAME, SERVICE_ACCOUNT_FILE, WORKSHEET_INDEXES

gs = gspread.service_account(SERVICE_ACCOUNT_FILE)
sheets = {
    name: gs.open(SPREADSHEET_NAME).get_worksheet(index)
    for name, index in WORKSHEET_INDEXES.items()
}
