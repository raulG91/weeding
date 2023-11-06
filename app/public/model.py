from flask import current_app
import googleapiclient.discovery
from google.oauth2 import service_account
from datetime import datetime
from flask_mail import Message,Mail



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
        

    def send_mail(self,name,last_name,email,message):
        email_object = Mail(current_app)
        email_object.connect()
        msg = Message(subject="Hola",
              sender="bodamariaraul105@gmail.com",
              recipients=["rgarciapedrosa@gmail.com"])
        msg.body = 'Bienvenid@ a j2logo'
        msg.html = '<p>Bienvenid@ a <strong>j2logo</strong></p>'
        email_object.send(msg)
        print("Sent")
     