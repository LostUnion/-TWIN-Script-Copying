import time
import json
from sessions import *
from requests.exceptions import RequestException
from impersonate_as_admin import login_as_admin

def get_admin_info(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId):
    URL = f"https://iam.twin24.ai/api/v1/users?companyId={cabinet}"
    
    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8',
        'User-Agent': user_agent,
        'x-xsrf-token': super_xsrf_token,
        'Authorization': f'Bearer {super_token}'}
    
    res = session_7.get(URL, headers=headers, data=payload)
    res_json = res.json()
    
    for item in res_json['items']:
        for role in item['roles']:
            if role['name'] == 'COMPANY_ADMIN':
                admin_user_id = item['id']
                email_user = item['email']
                break
            
    cookies_dict = [{"domain" : key.domain,
                             "name" : key.name,
                             "path" : key.path,
                             "value" : key.value} for key in session_7.cookies]
    for cookies in cookies_dict:
            session_8.cookies.set(**cookies)  
        
    print(f"[Status {res.status_code}] Company administrator found | ID: {admin_user_id} email: {email_user}")
    login_as_admin(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId, admin_user_id, email_user)