from flask import current_app
import googleapiclient.discovery
from google.oauth2 import service_account
from datetime import datetime

class Model:
    def __init__(self) -> None:
        pass
    def get_credentials(self):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        GOOGLE_PRIVATE_KEY = current_app.config.get('GOOGLE_PRIVATE_KEY')
    
        account_info = {
            "private_key": GOOGLE_PRIVATE_KEY,
            "client_email": current_app.config.get('GOOGLE_CLIENT_EMAIL'),
            "token_uri": "https://accounts.google.com/o/oauth2/token",
        }
    
        credentials = service_account.Credentials.from_service_account_info(account_info, scopes=SCOPES)
        return credentials
    def get_service(self,service_name='sheets', api_version='v4'):
        credentials = self.get_credentials()
        service = googleapiclient.discovery.build(service_name, api_version, credentials=credentials)
        return service

    def insert_invitee(self,name,last_name,email,phone,number,child_menu,alergies,bus):
       
        if bus == "True":
            bus = 'X'
        else:
            bus = '' 
        service = self.get_service()
        spreadsheet_id = current_app.config.get('GOOGLE_SHEET_ID')
        range_name = current_app.config.get('GOOGLE_SHEET_RANGE')
        # Call the Sheets API
        sheet = service.spreadsheets()
        object = {
            "majorDimension": "ROWS",
            "range" : range_name,
            "values":[[str(datetime.today()),name,last_name,phone,email,number,child_menu,alergies,bus]]
        }
        result = sheet.values().append(spreadsheetId=spreadsheet_id,
                                        range=range_name,body = object,insertDataOption= "INSERT_ROWS",valueInputOption="USER_ENTERED").execute()
        print(name + " " + last_name +" "+ phone + " "+ number + " " + number + " " + child_menu + " "+ alergies + bus)