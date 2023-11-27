from flask import current_app
import googleapiclient.discovery
from google.oauth2 import service_account
from datetime import datetime
from email.message import EmailMessage
import smtplib

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
        

    def send_mail(self,name,last_name,email,phone,message_user):
        remitente = current_app.config.get('FROM')
        destinatario = current_app.config.get('TO')
        credentials = current_app.config.get('PASSWORD')
        mensaje = f"Hola! \n  {name} {last_name} ha contactado con el siguiente mensaje \n {message_user} \n los datos de contacto son:\n Telefono: {phone} \n Email: {email}"
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Nuevo mensaje boda"
        email.set_content(mensaje)
        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(remitente, credentials)
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()    
    
        
        '''
        #SCOPES = ['https://www.googleapis.com/auth/gmail.addons.current.action.compose']
        SCOPES = ['https://www.googleapis.com/auth/gmail.send']
        GOOGLE_PRIVATE_KEY = current_app.config.get('GOOGLE_PRIVATE_KEY')
    
        account_info = {
            "private_key": GOOGLE_PRIVATE_KEY,
            "client_email": current_app.config.get('GOOGLE_CLIENT_EMAIL'),
            "token_uri": "https://accounts.google.com/o/oauth2/token",
        }
        credentials = service_account.Credentials.from_service_account_info(account_info, scopes=SCOPES)
        delegated_credentials = credentials.with_subject("rgarciapedrosa@gmail.com")
        service = googleapiclient.discovery.build("gmail", "v1", credentials= delegated_credentials)
        message = EmailMessage()
        message.set_content("This is automated draft mail")

        message["To"] = "rgarciapedrosa@gmail.com"
        #message["From"] = "bodamariaraul105@gmail.com"
        message["From"] = "rgarciapedrosa@gmail.com"
        message["Subject"] = "Automated draft"
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        print(encoded_message)
        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
    )
    '''
    
