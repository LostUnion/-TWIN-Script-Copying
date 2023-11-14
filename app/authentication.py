import json
from app.sessions import *
from requests.exceptions import RequestException
from app.update_cookies import cookies_update
from app.database import db_auth, get_login, get_password, delete_login_and_password

def auth(script, cabinet):
    while True:
        db_auth()
    
        login = get_login()
        password = get_password()
    
        URL = "https://iam.twin24.ai/api/v1/auth/login/"
    
        payload = json.dumps({"email" : login, "password" : password})
        headers = {"accept" : "application/json",
                   "content-type" : "application/json",
                   "User-Agent": user_agent,
                   "Authorization" : f"Bearer null"}
        try:
            res = session_1.post(URL, headers=headers, data=payload, timeout=10)
            if res.status_code == 200:
                super_token = res.cookies.get('token')
                super_refresh_token = res.cookies.get('refresh_token')
                break
            else:
                print(f'[STATUS {res.status_code}] Invalid username or password')
                delete_login_and_password()
                db_auth()
        except RequestException as rerr:
            print(rerr)
    
    cookies_dict = [{"domain" : key.domain, 
                     "name" : key.name, 
                     "path" : key.path, 
                     "value" : key.value} for key in session_1.cookies]
    for cookies in cookies_dict:
        session_2.cookies.set(**cookies)
        
    if res.status_code == 200:
        print(f'[Status {res.status_code}] Successful login to the account {login}')
        cookies_update(super_token, super_refresh_token, script, cabinet)