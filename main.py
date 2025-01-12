#hnaya ktbld les information dyalk

gmail="2003011700329@ofppt-edu.ma"
modpass="Moha2003med@"

##################################################################


# import psutil
# for process in psutil.process_iter(attrs=['pid', 'name']):
#     if process.info['name'] in ('chrome.exe', 'chromedriver.exe'):
#         process.terminate()  # إنهاء العملية

from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

def setup_driver():
    user_data_dir = r"chrome_user_data"
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}")  # استخدام مجلد ملف تعريف المستخدم
    # options.add_argument("--profile-directory=Default")  # تحديد ملف التعريف الافتراضي

    options.add_argument("--headless=new")           #ila briti Tb9a tchof ach kytra 7Ydi had line
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--mute-audio")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
    )
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver = uc.Chrome(options=options)
    return driver



# وظيفة لتسجيل الدخول
def login(driver, email, password):
    try:
        driver.get("https://app.ofppt-langues.ma/gw/api/saml/init?idp=https://sts.windows.net/dae54ad7-43df-47b7-ae86-4ac13ae567af/")
        send_key(driver, '//*[@id="i0116"]', email)
        click_element_with_mouse(driver, '//*[@id="idSIButton9"]')
        send_key(driver, '//*[@id="i0118"]', password)
        click_element_with_mouse(driver, '//*[@id="idSIButton9"]')
        click_element_with_mouse(driver, '//*[@id="idSIButton9"]')
        print("we login into the account")
        
    except Exception as e:
        print(f"Error in login: {e}")
        


# وظيفة لإرسال مفتاح
def send_key(driver, xpath, key):
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(key)
    except Exception as e:
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
        print(f"Error in click_element_with_mouse: {e}")


def click_element_with_css_selector(driver, css_selector):
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        actions = ActionChains(driver)
        actions.move_to_element(element)
        time.sleep(random.uniform(2, 5))
        actions.click().perform()
        time.sleep(random.uniform(2, 5))  # تأخير عشوائي لمحاكاة السلوك البشري
    except Exception as e:
        print(f"Error in click_element_with_css_selector: {e}")



# وظيفة لتجاوز الفيديو
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
        print(f"Error in wait_video: {e}")


    


def get_all_elements(driver, Selector):
    try:
        # انتظار ظهور العنصر الأساسي
        container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Selector))
        )
        # الحصول على جميع العناصر داخل العنصر الأساسي
        elements = container.find_elements(By.XPATH, "*")
        new_elements=[]
        for element in elements:
            CenvertSelector = driver.execute_script("""
                            const el = arguments[0];
                            const tag = el.tagName.toLowerCase();
                            const id = el.id ? '#' + el.id : '';
                            const classes = el.className && typeof el.className === 'string' ? '.' + el.className.replace(/ /g, '.') : '';
                            return tag + id + classes;
                        """, element)
            new_elements.append(CenvertSelector)


        selectors=[]
        for i in range(1,(len(new_elements)+1)):
            selector=f'#theme-provider > div.c-bUvWKu > main > div > div:nth-child(3) > div.c-gAkLYW > a:nth-child({i})'
            selectors.append(selector)
        return selectors


     
    except Exception as e:
        print('eroor in get_all_elements: ',e)







# الوظيفة الرئيسية
def main():
    driver = setup_driver()
    print("welcom to jalim script")
    try:
        # login(driver, gmail, modpass)
        
        lessons=[]
        for i in range(1,2):
            lesson=f'#VOCABULARY > ul > li:nth-child({i})'
            lessons.append(lesson)
        
        
        while True:
            driver.get('https://app.ofppt-langues.ma/gw/api/saml/init?idp=https://sts.windows.net/dae54ad7-43df-47b7-ae86-4ac13ae567af/')
            time.sleep(10)
            driver.get("https://app.ofppt-langues.ma/platform/discover")
            time.sleep(3)
            # تحقق من أن الرابط الحالي هو الرابط المطلوب
            if driver.current_url == "https://app.ofppt-langues.ma/platform/discover":
                print("we got the page !")
            else:
                print(f"the current page is: {driver.current_url}")
                continue


            for lesson in lessons:
                n=0
                click_element_with_css_selector(driver, lesson)

                # التعامل مع الدروس
                tip_selectors = get_all_elements(driver, '#theme-provider > div.c-bUvWKu > main > div > div:nth-child(3) > div')
                for tip in tip_selectors:
                    click_element_with_css_selector(driver, tip)
                    click_element_with_css_selector(driver, '#theme-provider > div.c-bUvWKu > main > div > ul.c-dYOPMy > li:nth-child(1)')
                    wait_video(driver)
                    time.sleep(21600)
                    click_element_with_mouse(driver, '//*[@id="theme-provider"]/div[1]/main/div/div[2]/a')
                    click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > ul.c-dXWjRp > li:nth-child(2)')
                    n+=1
                    print(n)
                    if tip==tip_selectors[-1]:
                        click_element_with_css_selector(driver,'#theme-provider > div.c-bUvWKu > main > div > ul.c-dXWjRp > li:nth-child(1)')
                        print('done!')
    except Exception as e:
        print(f"Error in main loop: {e}")
    finally:
        driver.quit()


# بدء التنفيذ
if __name__ == "__main__":
    main()
