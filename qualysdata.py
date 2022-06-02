__author__    = 'Donald Whitfield'
__copyright__ = 'Johnson Controls International'
__email__     = 'donald.r.whitfield@jci.com'
__satus__     = 'Development Version'

import os
import json
from dotenv import load_dotenv
import requests
import xml.etree.ElementTree as ET


class QualysAPI:
    def __init__(self, auth_url, header, file_name, api_endpoint, username, password):
        self.auth_url = auth_url
        self.file_name = file_name
        self.username = username
        self.password = password
        self.api_endpoint = api_endpoint
        self.api_endpoint = api_endpoint
        self.headers = headers


load_dotenv()

USERNAME = os.getenv("USER_ID")
PASSWORD = os.getenv("PASSWORD")


def GetAssets():

    #
    # ---Pull Qualys Asset Groups for Tenant Associated with Account---
    #

    global headers
    headers = {"X-Requested-With": "Python Auth"}

    global payload
    payload = {
               'action':'login',
               'username': USERNAME,
               'password': PASSWORD
               }


    global auth_url
    auth_url = "https://qualysguard.qg2.apps.qualys.eu/api/2.0/fo/session/"
    assets_url = "https://qualysguard.qg2.apps.qualys.eu/api/2.0/fo/asset/group/?action=list"

    filename = "QualysAssetData.xml"
    file_mode = "w"

    with requests.Session() as session:
        post = session.post(auth_url, headers=headers, data=payload)
        r = session.get(assets_url, headers=headers)
        print(r.text)

    with open(filename, file_mode) as f:
            f.write(r.text)

'''        
        file = open("QualysAssetData.xml", "a")
        file.write(r.text)
        file.close()
'''



def GetSchedScans():

    filename = "QualysNetworksData.xml"
    file_mode = "w"
    networks_url = "https://qualysguard.qg2.apps.qualys.eu/api/2.0/fo/schedule/scan/?action=list"

    with requests.Session() as session:
        post = session.post(auth_url, headers=headers, data=payload)
        r = session.get(networks_url, headers=headers)
        print(r.text)
        
        with open(filename, file_mode) as f:
            f.write(r.text)
            
            
'''
        file = open("QualysNetworksData.xml", "a")
        file.write(r.text)
        file.close()
'''


GetAssets()
GetSchedScans()