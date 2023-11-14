import time
from app.sessions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.checking_for_correct_saving import correct_saving

def script_saving(new_botId, admin_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Chrome(options=options)

    URL = f"https://tcl.twin24.ai/editor/{new_botId}?token={admin_token}&ai=null"
    print("[SAVING] Opening the browser to save")

    driver.get(URL)
    time.sleep(2)

    print("[SAVING] Updating the browser page")
    driver.refresh()
    time.sleep(10)
    while True:
        try:
            print("[SAVING] Saving the script")
            save_button = driver.find_element(By.CLASS_NAME, "fa.fa-save")
            save_button.click()

            print("[SAVING] Waiting for the result of saving")
        except:pass
    
        try:
            wait_welcome = WebDriverWait(driver, 30)
            wait_welcome.until(EC.visibility_of_element_located((By.CLASS_NAME,"swal2-popup.swal2-modal.swal2-show")))
            driver.refresh()
        except:pass
        try:
            wait_alert = driver.switch_to.alert
            print(f"[SAVING] Alert Text: {wait_alert.text}")
            time.sleep(0.5)
            wait_alert.accept()
            print("[SAVING] Allert accepted")
        except:pass

        try:
            wait_succes = WebDriverWait(driver, 10000)
            wait_succes.until(EC.visibility_of_element_located((By.CLASS_NAME, "swal2-icon.swal2-success.swal2-animate-success-icon")))
            ok_button = driver.find_element(By.CLASS_NAME, "swal2-confirm.swal2-styled")
            ok_button.click()
            print("[SAVING] Success!")
            time.sleep(1)
            print("[SAVING] Closing the browser window")
            time.sleep(1)
            driver.close()
            
            correct_saving(new_botId, admin_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session)
            break
        except:
            pass
    
    

    
    
    
    
    
    
