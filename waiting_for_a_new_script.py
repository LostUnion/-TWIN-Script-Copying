import time
import json
from sessions import *
from requests.exceptions import RequestException
from get_company_admin import get_admin_info


def search_for_migrated_script(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId):
    print("[SEARCH] Search for a new script. Please await...")
    
    while True:
        URL = f"https://bot.twin24.ai/api/v1/bots/{new_botId}"
        payload = {}
        headers = {
            "User-Agent": user_agent,
            "Authorization": f"Bearer {super_token}"
        }
        
        res = session_6.get(URL, headers=headers, data=payload, timeout=100)
        
        if res.status_code == 200:
            print(f'[Status {res.status_code}] [+] The script "{name}" is copied to the cabinet {cabinet}') 
                     
            cookies_dict = [{"domain" : key.domain,
                             "name" : key.name,
                             "path" : key.path,
                             "value" : key.value} for key in session_6.cookies]
            for cookies in cookies_dict:
                session_7.cookies.set(**cookies)
            
            get_admin_info(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId)
            break
        elif res.status_code == 404:
            time.sleep(5)
            pass