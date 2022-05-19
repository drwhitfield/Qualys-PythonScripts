__author__    = 'Donald Whitfield'
__copyright__ = 'Johnson Controls International'
__email__     = 'donald.r.whitfield@jci.com'
__satus__     = 'Development Version'

import os
from dotenv import load_dotenv
import requests
import xml.etree.ElementTree as ET


load_dotenv()

USERNAME = os.getenv("USER_ID")
PASSWORD = os.getenv("PASSWORD")


def login():

    #
    # ---Session Login Code---
    #

    payload = {
               'action':'login',
               'username': USERNAME,
               'password': PASSWORD
               }
    
    response = requests.post('https://qualysguard.qg2.apps.qualys.eu/api/2.0/fo/scan/', data=payload)
    print(response)

    # Now that all the hard work was done, we can parse the response.
    xmlreturn = ET.fromstring(response.text)
    for elem in xmlreturn.findall('.//TEXT'):
        print (elem.text) #Prints the "Logged in" message. Not really needed, but reassuring.

login()
