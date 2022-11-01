from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1y_hYCHWU3yF2d2dUXM3qcnYuXCgwVcglC18Ls_uFz0A'


def main():
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Contact!A1:E4").execute()
    # values = result.get('values', [])

    print(result)

    # if not values:
    #     print('No data found.')
    #     return
    #
    # else:
    #     print('Name, Major:')
    #     for row in values:
    #         # Print columns A and E, which correspond to indices 0 and 4.
    #         print('%s, %s' % (row[0], row[4]))


if __name__ == '__main__':
    main()
