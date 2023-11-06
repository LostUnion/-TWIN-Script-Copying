import requests
from requests import RequestException
import json
import time
import argparse
import io
from fake_useragent import UserAgent

session = requests.Session()
session_2 = requests.Session()
user_agent = UserAgent().random
    
def new_snapshot(token, refresh_token, script, XSRF_TOKEN, ID, name):
    URL = f"https://tcl.twin24.ai/superadmin/scripts/snapshot/new/{ID}"
    
    payload = {'comment' : name}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8',
        'User-Agent': user_agent,
        'x-xsrf-token': XSRF_TOKEN,
        'Authorization': f'Bearer {token}'
    }
    time.sleep(3)
    response = session_2.post(URL, headers=headers, json=payload, timeout=1000)
    StatusCode = response.status_code
    
    if StatusCode == 201:
        print(f'[Status {response.status_code}] New snapshot')
    elif StatusCode == 500:
        print(f'[Status {response.status_code}] Unexpected error on the server side')
        update_cookies(token, refresh_token, script)
        

def get_bot_info(token, refresh_token, script, XSRF_TOKEN):
    URL = f"https://bot.twin24.ai/api/v1/bots/{script}?fields=id,name,companyId"
    
    payload = {}
    headers = {
        "Authorization": f'Bearer {token}',
        'User-Agent': user_agent,
        "Content-Length" : "0"
    }
    
    response = session_2.get(URL, headers=headers, data=payload, timeout=5)
    response_json = response.json()
    
    ID = response_json.get('id')
    name = response_json.get('name')
    companyId = response_json.get('companyId')
    
    print(f'[Status {response.status_code}] {companyId} | {name} | {ID}')
    new_snapshot(token, refresh_token, script, XSRF_TOKEN, ID, name)
    

def update_cookies(token, refresh_token, script):
    URL = "https://tcl.twin24.ai/"
    
    payload = {}
    headers = {
        'User-Agent': user_agent,
        "Authorization" : f"Bearer {token}"}
    
    response = session.get(URL, headers=headers, data=payload, timeout=5)
    
    XSRF_TOKEN = response.cookies.get('XSRF-TOKEN')
    
    cookies_dict = [
        {"domain" : key.domain, "name" : key.name, "path" : key.path, "value" : key.value}
        for key in session.cookies
    ]
    
    for cookies in cookies_dict:
        session_2.cookies.set(**cookies)
    
    print(f'[Status {response.status_code}] Update Cookies')
    get_bot_info(token, refresh_token, script, XSRF_TOKEN)

def authentication(login, password, script):
    URL = "https://iam.twin24.ai/api/v1/auth/login/"
    
    payload = json.dumps({"email" : login, "password" : password})
    headers = {"accept" : "application/json",
               "content-type" : "application/json",
               'User-Agent': user_agent,
               "Authorization" : f"Bearer null"}
    
    response = requests.post(URL, headers=headers, data=payload, timeout=10)
    
    token = response.cookies.get('token')
    refresh_token = response.cookies.get('refresh_token')
    
    print(f'[Status {response.status_code}] Successful login to the account {login}')
    update_cookies(token, refresh_token, script)

def prymary_function(login, password, script, cabinet):
    authentication(login, password, script)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copying a script from a superadmin')
    parser.add_argument('-l', '--login', type=str, required=True, help='Your superuser login from the Twin cabinet')
    parser.add_argument('-p', '--password', type=str, required=True, help='Your superuser password from the Twin cabinet')
    parser.add_argument('-s', '--script', type=str, help='ID of the script to copy')
    parser.add_argument('-c', '--cabinet', type=int, help='ID of the cabinet to copy the script to')
    
    args = parser.parse_args()
    prymary_function(args.login,
                     args.password,
                     args.script,
                     args.cabinet)
    
