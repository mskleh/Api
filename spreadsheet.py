"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pprint

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('credentials.json')
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('clientSpreadsheetAPI.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API for fundamental ratio variable
def fetchSpreadSheet():
    SPREADSHEET_ID = '1K4p9lYs2e3eHL5J63ZRyd7gS7RqKkzBmWUtVLT6PSW8'
    RANGE_NAME = 'stock!A2:B'
    try:
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
        values = result.get('values', [])
        if not values:
            return ('No data found.')
        else:
            # Reformatting into object
            data = {}
            for row in values:
                data[row[1]] = row[0]
            return data
    except:
        return ('Error occur during communicating with Google Spreadsheet API')