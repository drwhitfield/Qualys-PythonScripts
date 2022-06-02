__author__    = 'Donald Whitfield'
__copyright__ = 'Johnson Controls International'
__email__     = 'donald.r.whitfield@jci.com'
__satus__     = 'Development Version'

import os
import json
from wsgiref import headers
from dotenv import load_dotenv
import requests
import xml.etree.ElementTree as ET


class QualysAPI:
    def __init__(self, auth_url, headers, file_name, api_endpoint, username, password, auth_params):
        self.auth_url = auth_url
        self.file_name = file_name
        self.username = username
        self.password = password
        self.api_endpoint = api_endpoint
        self.headers = headers
        self.auth_params = auth_params


load_dotenv()
USERNAME = os.getenv("USER_ID")
PASSWORD = os.getenv("PASSWORD")


def GetQualysAssets():

    #
    # ---Pull Qualys Asset Groups for Tenant Associated with Account---
    #

    
    QualysAPI.headers = {"X-Requested-With" : "Python_API_Header"}
    QualysAPI.auth_params = {
               'action':'login',
               'username': USERNAME,
               'password': PASSWORD
               }


    QualysAPI.auth_url = "https://qualysguard.qg2.apps.qualys.eu/api/2.0/fo/session/"
    assets_url = "https://qualysguard.qg2.apps.qualys.eu/api/2.0/fo/asset/group/?action=list"

    filename = "QualysAssetData.xml"
    file_mode = "w"

    with requests.Session() as session:
        push_data = session.post(QualysAPI.auth_url, headers=QualysAPI.headers, data=QualysAPI.auth_params)
        pull_data = session.get(assets_url, headers=QualysAPI.headers)
        print(pull_data.text)


    try:
        with open(filename, file_mode) as f:
            f.write(pull_data.text)
    except FileNotFoundError:
        print("There Was An Issue Finding The Requested File")




def GetQualysSchedScans():

    #
    # ---Pull Qualys Network Asset Data for Tenant Associated with Account---
    #

    filename = "QualysNetworksData.xml"
    file_mode = "w"
    
    networks_url = "https://qualysguard.qg2.apps.qualys.eu/api/2.0/fo/schedule/scan/?action=list"

    with requests.Session() as session:
        push_data = session.post(QualysAPI.auth_url, headers=QualysAPI.headers, data=QualysAPI.auth_params)
        pull_data = session.get(networks_url, headers=QualysAPI.headers)
        print(pull_data.text)
        

    try:
        with open(filename, file_mode) as f:
            f.write(pull_data.text)
    except FileNotFoundError:
            print("There Was An Issue Finding The Requested File")
            



GetQualysAssets()
GetQualysSchedScans()