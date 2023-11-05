import requests
from requests import RequestException
import json
import time
import argparse

def new_snapshot(token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token, UUID, ID, name):
    # Функция новый снапшот
    # 1. Аргумент ID передается в URL
    # 2. Аргумент name передается в payload
    # 3. Аргументы XSRF_TOKEN, token, laravel_session, laravel_token, UUID передаются в headers запроса
    
    '''Далее наблюдается странное поведение сервера 
    При выводе response.content:
    status_code 419 c сообщением b'{\n    "message": ""\n}'
    status_code 500 с сообщением b'{\n    "message": "Server Error"\n}
    '''
    
    URL = f"https://tcl.twin24.ai/superadmin/scripts/snapshot/new/{ID}"
    
    payload = {"comment" : name}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8',
        'x-xsrf-token': XSRF_TOKEN,
        'Authorization': f'Bearer {token}',
        'Cookies' : f'XSRF-TOKEN={XSRF_TOKEN};laravel_session={laravel_session};laravel_token={laravel_token};sessionid={UUID}'
    }
    
    response = requests.post(URL, headers=headers, data=payload)
    while response.status_code == 500:
        response = requests.post(URL, headers=headers, data=payload)
        print(f'[Status {response.status_code}] New snapshot')
    print(f'[Status {response.status_code}] New snapshot')
    
    

def get_bot_info(token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token, UUID):
    # Функция получения информации о сценарии.
    # 1. Аргумент token передается в поле Authorization.
    # 2. При GET запросе с заданными параметрами, в JSON ответе приходят id, name, companyId
    # 4. Полученные значения записываются в переменные, затем выводятся.
    # 5. Запускается функция new_snapshot c аргументами token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token, UUID, ID, name
    
    URL = f"https://bot.twin24.ai/api/v1/bots/{script}?fields=id,name,companyId"
    
    payload = {}
    headers = {
        "Authorization": f'Bearer {token}',
        "Content-Length" : "0"
    }
    
    response = requests.get(URL, headers=headers, data=payload)
    response_json = response.json()
    
    ID = response_json.get('id')
    name = response_json.get('name')
    companyId = response_json.get('companyId')
    
    print(f'[Status {response.status_code}] {companyId} | {name} | {ID}')
    new_snapshot(token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token, UUID, ID, name)
    

def update_cookies(token, refresh_token, script):
    # Функция обновления cookies.
    # 1. Аргумент token передается в поле Authorization.
    # 2. При GET запросе с заданными параметрами, в cookies ответе приходят laravel_token, XSRF-TOKEN, laravel_session
    # 3. При GET запросе с заданными параметрами, в headers ответе приходит X-Request-ID
    # 4. Полученные значения записываются в переменные.
    # 5. Запускается функция update_cookies c аргументами token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token, UUID
    
    URL = "https://tcl.twin24.ai/"
    
    payload = {}
    headers = {"Authorization" : f"Bearer {token}"}
    response = requests.get(URL, headers=headers, data=payload)
    
    XSRF_TOKEN = response.cookies.get('XSRF-TOKEN')
    laravel_session = response.cookies.get('laravel_session')
    laravel_token = response.cookies.get('laravel_token')
    UUID = response.headers.get('X-Request-ID')
    
    print(f'[Status {response.status_code}] Update Cookies')
    get_bot_info(token, refresh_token, script, XSRF_TOKEN, laravel_session, laravel_token, UUID)

def authentication(login, password, script):
    
    # Функция аунтификации.
    # 1. Аргументы login, password передаются в payload.
    # 2. При POST запросе с задаными параметрами, в cookies ответе приходят token, refresh_token
    # 3. Полученные значения записываются в переменные.
    # 4. Запускается функция update_cookies c аргументами token, refresh_token, script
    
    URL = "https://iam.twin24.ai/api/v1/auth/login/"
    
    payload = json.dumps({"email" : login, "password" : password})
    
    headers = {"accept" : "application/json",
               "content-type" : "application/json",
               "Authorization" : f"Bearer null"}
    
    response = requests.post(URL, headers=headers, data=payload)
    
    print(f'[Status {response.status_code}] Successful login to the account {login}')
    
    token = response.cookies.get('token')
    refresh_token = response.cookies.get('refresh_token')
    
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
    
