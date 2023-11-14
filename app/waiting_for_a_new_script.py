import asyncio
from app.sessions import *
from app.get_company_admin import get_admin_info

async def animate_loading():
    anim = '|/-\\'
    i = 0
    while True:
        element = anim[i % len(anim)]
        print(f'[LOADING] Script search in account. Please await {element}', end="\r")
        await asyncio.sleep(0.1)
        i += 1

async def check_status(loading_task, super_token, cabinet, super_xsrf_token, name, new_botId):
    while True:
        URL = f"https://bot.twin24.ai/api/v1/bots/{new_botId}"
        payload = {}
        headers = {
            "User-Agent": user_agent,
            "Authorization": f"Bearer {super_token}"
        }
        
        res = session_6.get(URL, headers=headers, data=payload, timeout=100)
        if res.status_code == 200:
            print(f'\n[Status {res.status_code}] [+] The script "{name}" is copied to the cabinet {cabinet}') 
                     
            cookies_dict = [{"domain" : key.domain,
                             "name" : key.name,
                             "path" : key.path,
                             "value" : key.value} for key in session_6.cookies]
            for cookies in cookies_dict:
                session_7.cookies.set(**cookies)
            
            get_admin_info(super_token, cabinet, super_xsrf_token, new_botId)
            loading_task.cancel()
            break
        elif res.status_code == 404:
            await asyncio.sleep(10)
            pass

async def main(super_token, cabinet, super_xsrf_token, name, new_botId):
    loading_task = asyncio.create_task(animate_loading())
    status_task = asyncio.create_task(check_status(loading_task, super_token, cabinet, super_xsrf_token, name, new_botId))

    await status_task

def check_script(super_token, cabinet, super_xsrf_token, name, new_botId):
    asyncio.run(main(super_token, cabinet, super_xsrf_token, name, new_botId))
