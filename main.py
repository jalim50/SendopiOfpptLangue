
gmail="2003011700329@ofppt-edu.ma"
modpass="Moha2003med@"








from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


# إعدادات السائق
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--mute-audio")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
    )
    driver = uc.Chrome(options=options)
    return driver


# وظيفة لتسجيل الدخول
def login(driver, email, password):
    try:
        driver.get("https://app.ofppt-langues.ma/gw/api/saml/init?idp=https://sts.windows.net/dae54ad7-43df-47b7-ae86-4ac13ae567af/")
        time.sleep(1)
        send_key(driver, '//*[@id="i0116"]', email)
        time.sleep(1)
        click_element_with_css_selector(driver,'#idSIButton9')
        time.sleep(1)
        send_key(driver, '//*[@id="i0118"]', password)
        time.sleep(1)
        click_element_with_css_selector(driver,'#idSIButton9')
        time.sleep(1)
        click_element_with_css_selector(driver,'#idSIButton9')
        time.sleep(1)
        print('we  login into the account ')
        
    except Exception as e:
        print('login error')
        print("Current Time:",  time.strftime("%H:%M:%S", time.localtime()))
        print(f"Error in login: {e}")
        
        


# وظيفة لإرسال مفتاح
def send_key(driver, xpath, key):
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(key)
    except Exception as e:
        print("Current Time:",  time.strftime("%H:%M:%S", time.localtime()))
        print(f"Error in send_key: {e}")


# وظيفة للنقر
def click_element_with_mouse(driver, xpath):
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
        actions = ActionChains(driver)
        actions.move_to_element(element)
        time.sleep(random.uniform(2, 5))
        actions.click().perform()
        time.sleep(random.uniform(2, 5))
    except Exception as e:
        print("Current Time:",  time.strftime("%H:%M:%S", time.localtime()))
        print(f"Error in click_element_with_mouse: {e}")


def click_element_with_css_selector(driver, css_selector):
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        element.click()
        time.sleep(random.uniform(2, 5))  # تأخير عشوائي لمحاكاة السلوك البشري
    except Exception as e:
        print("Current Time:",  time.strftime("%H:%M:%S", time.localtime()))
        print(f"Error in click_element_with_css_selector: {e}")
        

def skip_video(driver):
    try:
        video =  WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#theme-provider > div.c-bUvWKu > main > div > div > div.c-bQzyIt.c-bQzyIt-kqOPqT-alignContent-start.c-bQzyIt-ddIBXx-gap-4 > div > div > div.plyr__video-wrapper > video')))
        time.sleep(random.uniform(2, 5))
        video_duration = driver.execute_script("return arguments[0].duration;", video)
        start_time = video_duration - 3
        driver.execute_script(f"arguments[0].currentTime = {start_time};", video)
        driver.execute_script("arguments[0].play();", video)
    except Exception as e:
        print(f"Error in skip_video: {e}")

    
def wait_video(driver):
    try:
        video =  WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#theme-provider > div.c-bUvWKu > main > div > div > div.c-bQzyIt.c-bQzyIt-kqOPqT-alignContent-start.c-bQzyIt-ddIBXx-gap-4 > div > div > div.plyr__video-wrapper > video')))
        time.sleep(random.uniform(2, 5))
        video_duration = driver.execute_script("return arguments[0].duration;", video)
        driver.execute_script("arguments[0].play();", video)
        time.sleep(video_duration+1)
    except Exception as e:
        print(f"Error in skip_video: {e}")




# الوظيفة الرئيسية
def main():
   
    driver = setup_driver()
    try:
        
        login(driver, gmail, modpass)
        time.sleep(60)
        driver.get("https://www.google.com")
        time.sleep(40)
        n=0
        driver.get("https://app.ofppt-langues.ma/platform/discover")
        while True:
            # تحقق من أن الرابط الحالي هو الرابط المطلوب
            if driver.current_url == "https://app.ofppt-langues.ma/platform/discover":
                print("we got the page !")
            else:
                print(f"we did not get the page the current page is : {driver.current_url}",  time.strftime("%H:%M:%S", time.localtime()))
                
                time.sleep(20)
                driver.get("https://app.ofppt-langues.ma/platform/discover")
                click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > header > nav > ul > li:nth-child(2) > a')
                continue

            click_element_with_css_selector(driver,'#VOCABULARY > ul > li:nth-child(1) > a > p')
            for i in range(1,6):
                click_element_with_css_selector(driver,f'#theme-provider > div.c-bUvWKu > main > div > div:nth-child(3) > div > a:nth-child({i})')
                click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > ul.c-dYOPMy > li:nth-child(1)')
                click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > div > div.c-bQzyIt.c-bQzyIt-kqOPqT-alignContent-start.c-bQzyIt-ddIBXx-gap-4 > div > div > button')
                skip_video(driver)
                click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > div.c-UazGY.c-UazGY-hySSfO-gap-12')
                click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > ul.c-dXWjRp > li:nth-child(2)')
            click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > ul.c-dXWjRp > li:nth-child(1)')

                
            n+=1
            print(n)
            
            


    except Exception as e:
        print("Current Time:",  time.strftime("%H:%M:%S", time.localtime()))
        print(f"Error in main loop: {e}")
    finally:
        driver.quit()


# بدء التنفيذ
if __name__ == "__main__":
    main()
