import requests
import json
import time
import argparse

session_1 = requests.Session()

def new_snapshot(token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token, ID, name):
    URL = f"https://tcl.twin24.ai/superadmin/scripts/snapshot/new/{ID}"
    
    payload = {"comment" : name}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8',
        'x-xsrf-token': f'{refresh_token}',
        "Authorization": f'Bearer {token}'

    }
    response = requests.post(URL, headers=headers, data=payload)
    print(response.status_code)
    while response.status_code == 500:
        response = session_1.post(URL, headers=headers, data=payload)
        time.sleep(5)
        print(response.status_code)
    
    

def get_bot_info(token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token):
    URL = f"https://bot.twin24.ai/api/v1/bots/{script}?fields=id,name,companyId"
    
    payload = {}
    headers = {
        "Authorization": f'Bearer {token}',
        "Content-Length" : "0"
    }
    
    response = session_1.get(URL, headers=headers, data=payload)
    response_json = response.json()
    
    ID = response_json.get('id')
    name = response_json.get('name')
    companyId = response_json.get('companyId')
    print(f'Компания: {companyId} | Сценарий: {name} | ID Сценария: {ID}')
    time.sleep(5)
    new_snapshot(token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token, ID, name)
    

def update_cookies(token, refresh_token, script):
    URL = "https://tcl.twin24.ai/"
    
    payload = {}
    headers = {"Authorization" : f"Bearer {token}"}
    response = session_1.get(URL, headers=headers, data=payload)
    
    XSRF_TOKEN = response.cookies.get('XSRF-TOKEN')
    laravel_session = response.cookies.get('laravel_session')
    laravel_token = response.cookies.get('laravel_token')
    
    time.sleep(5)
    get_bot_info(token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token)
    

def authentication(login, password, script):
    URL = "https://iam.twin24.ai/api/v1/auth/login"
    
    payload = json.dumps({"email" : login, "password" : password})
    
    headers = {"accept" : "application/json", 
               "content-type" : "application/json",
               "Authorization" : f"Bearer null"}
    
    
    response = session_1.post(URL, headers=headers, data=payload)
    
    print(f'[{response.status_code}] Successful login to the account {login}')
    
    token = response.cookies.get('token')
    refresh_token = response.cookies.get('refresh_token')
    
    time.sleep(5)
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
    
