from app.sessions import *
from app.update_cookies_admin import admin_cookies_update


def login_as_admin(super_token, super_xsrf_token, new_botId, admin_user_id, email_user):
    URL = f"https://iam.twin24.ai/api/v1/auth/impersonate/take/{admin_user_id}"
    
    payload = ""
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json;charset=UTF-8',
        'User-Agent': user_agent,
        'x-xsrf-token': super_xsrf_token,
        'Authorization': f'Bearer {super_token}'
    }
    res = session_8.post(URL, headers=headers, data=payload)  
    admin_token = res.cookies.get('token')
    
    cookies_dict = [{"domain" : key.domain,
                     "name" : key.name,
                     "path" : key.path,
                     "value" : key.value} for key in session_8.cookies]
    for cookies in cookies_dict:
            session_9.cookies.set(**cookies)  
    
    print(f'[Status {res.status_code}] [+] Log in to account {email_user}')
    admin_cookies_update(new_botId, email_user, admin_token)