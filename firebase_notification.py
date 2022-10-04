import json
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
import requests

def send_notification(record, userID, action):
    #Please add your firebase realtime database url
    url = 'https://joanna-project-test-default-rtdb.firebaseio.com/'
    # put data to firebase (create a new record)
    response = requests.put(f'{url}/tracker/{userID}/{action}.json', data=json.dumps(record))
    #print(response.content)
    #print(response)
    #print("Response sent")

