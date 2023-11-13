import time
from sessions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from checking_for_correct_saving import correct_saving


def script_saving(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId, admin_user_id, email_user, admin_token, admin_refresh_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session):
    
    URL = f"https://tcl.twin24.ai/editor/{new_botId}?token={admin_token}&ai=null"

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument(f"user-agent={user_agent}")

    driver = webdriver.Chrome(options=options)

    print("[SAVING] Opening the browser to save")

    driver.get(URL)
    time.sleep(5)

    print("[SAVING] Updating the browser page")
    
    
    
    driver.refresh()
    time.sleep(10)
    print("[SAVING] Saving the script")
    save_button = driver.find_element(By.CLASS_NAME, "fa.fa-save")
    save_button.click()
    print("[SAVING] Waiting for the result of saving")

    try:
        alert = driver.switch_to.alert
        print(f"[SAVING] Alert Text: {alert.text}")
        time.sleep(1)
        alert.accept()
        print("[SAVING] Allert accepted")
    except:
        pass
        
        
    wait_succes = WebDriverWait(driver, 30)
    wait_succes.until(EC.visibility_of_element_located((By.CLASS_NAME, "swal2-icon.swal2-success.swal2-animate-success-icon")))
    
    print("[SAVING] Success!")
    time.sleep(1)
    print("[SAVING] Closing the browser window")
    time.sleep(1)
    driver.close()
    correct_saving(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId, admin_user_id, email_user, admin_token, admin_refresh_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session)
    
