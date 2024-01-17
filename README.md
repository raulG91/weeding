# Weeding

Repository containing my weeding website. We used this website as invitation for all asistants to our weeding. It will contain all information about the event and it will allow user to confirm assistance to the event.

# Technology

- **Backend**: This is a flask application. Backend is done completly with python
- **Frontend**: It uses HTML, CSS and Javascript. Website is reponsible and will adapt the content to mobile devices.
- **Deploy**: Application was deployed into Google cloud and it uses a custom domain: https://www.bodamariaraul.net/

# Highlights

1. Reposnsible website
2. it includes a timeline with the events for selected date
3. Register form for invitees. It will store the data for atendees in a google drive sheet which will make easier for user to make modifications
4. Google maps showing hotel location

# Installation

1. Clone repository
2. If you already have a Google API project, select it. Otherwise, create one.
3. Click "CREATE SERVICE ACCOUNT"
4. Enter a Service account name and Description. Click "CREATE AND CONTINUE".
5. Set Role to Owner. Click "CONTINUE".
6. Under "3. Grant users access to this service account", leave both boxes blank and click "DONE".
7. Once back on the "Service accounts for project <project_name>" screen, click the "⋮" menu in the "Actions" column of your new Service Account and select "Manage Keys".
8. Click the "ADD KEY" dropdown and select "Create new key". On the "Create Private key for <project_name>" modal, ensure that the JSON Key type is select, and then click "CREATE".
9. Create and download json file
10. Activate your API for google maps. And change the script at the top of the `ìndex.html` with your API Key
11. Create configuration file `config.py` with the following constants:
    1.  `SECRET_KEY`: Secret key used for flask app.
    2.  `GOOGLE_PRIVATE_KEY`: Copy private key value from downloaded json file.
    3.  `GOOGLE_CLIENT_EMAIL`: Copy client email from downloaded json file.
    4.  `GOOGLE_SHEET_ID`: Id for your google sheet. Share your sheet with your `GOOGLE_CLIENT_EMAIL`
    5.  `GOOGLE_SHEET_RANGE`: Range to be used in the document
12. Install requirements file.
13. Run: flask --app main  run --debug  
14. Create `.yaml` file used to deploy the app in Google cloud

 