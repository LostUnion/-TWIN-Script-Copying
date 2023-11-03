import requests
import json
from config import *
import time


bot_id = 'eb3f747f-422b-4d01-9347-66f051f15686'

def new_snapshot(token, refresh_token, bot_id, bot_name, laravel_token, xSRF_TOKEN, laravel_session):
    botId = 'eb3f747f-422b-4d01-9347-66f051f15686'
    url = f"https://tcl.twin24.ai/superadmin/scripts/snapshot/new/{botId}"

    payload = {
        "comment": f"{bot_name}"
    }
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8',
        'x-xsrf-token': f'',
        'Authorization': f'Bearer {token}',
        'Cookie': f'XSRF-TOKEN={xSRF_TOKEN};laravel_session={laravel_session};laravel_token={laravel_token}'
    }

    response = requests.post(url, headers=headers, data=payload)
    print(f'[{response.status_code}] ERROR')
    
    
    
def get_bot_info(token, refresh_token, laravel_token, xSRF_TOKEN, laravel_session):
    bot_id = '3ca96f95-1767-40c6-8c61-1d9f6d391842'
    url = f"https://bot.twin24.ai/api/v1/bots/{bot_id}?fields=id,name,companyId"
    
    bearer = f'Bearer{token}'
    
    payload = {}
    headers = {
        'Authorization': bearer,
        'Content-Length' : '0'
    }
    
    response = requests.get(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        bot_id = response_json.get('id')
        bot_name = response_json.get('name')
        get_company_id = response_json.get('companyId')
        
        print(f'[{response.status_code}] Компания: {get_company_id} | Сценарий: {bot_name} | ID Сценария: {bot_id}')
        time.sleep(3)
        new_snapshot(token, refresh_token, bot_id, bot_name, laravel_token, xSRF_TOKEN, laravel_session)


def update_cookies(token, refresh_token):
    url = "https://tcl.twin24.ai/"
    
    token = token
    bearer = f'Bearer{token}'
    payload = {}
    
    headers = {
        'Authorization': bearer
    }
    
    response = requests.get(url, headers=headers, data=payload)
    laravel_token = response.cookies.get('laravel_token')
    xSRF_TOKEN = response.cookies.get('XSRF-TOKEN')
    laravel_session = response.cookies.get('laravel_session')
    
    # print(f'laravel_token = {laravel_token}\nxSRF_TOKEN = {xSRF_TOKEN}\n laravel_session = {laravel_session}')
    
    if response.status_code == 200:
        print(f'[{response.status_code}] Updates Cookies')
        get_bot_info(token, refresh_token, laravel_token, xSRF_TOKEN, laravel_session)
    
    while response.status_code != 200:
        print(f'[{response.status_code}] Updates Cookies')
        time.sleep(2)
        if response.status_code == 200:
            print(f'[{response.status_code}] Updates Cookies')
            time.sleep(3)
            get_bot_info(token, refresh_token, laravel_token, xSRF_TOKEN, laravel_session)
    
    
    
def authentication():
    url = "https://iam.twin24.ai/api/v1/auth/login"

    payload = json.dumps({
        "email": twin_email,
        "password": twin_password,
        })

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Authorization': 'Bearer null'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.cookies.get('token')
    refresh_token = response.cookies.get('refresh_token')
    
    if response.status_code == 200:
        print(f'[{response.status_code}] Authentication {twin_email}')
        time.sleep(3)
        update_cookies(token, refresh_token)
    
    while response.status_code != 200:
        print(f'[{response.status_code}] Failed, retrying no')
        time.sleep(2)
        if response.status_code == 200:
            print(f'[{response.status_code}] Authentication {twin_email}')
            time.sleep(3)
            update_cookies(token, refresh_token)
    
            
if __name__ == "__main__":
    authentication()



