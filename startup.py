from selenium import webdriver
import pyautogui
from time import sleep
#import utils.io_methods as iom
import os

#BASE_DIR = os.path.dirname(os.path.dirname("C:/Users/Admin/Desktop/charity_navigator/chromedriver"))

def config_startup():
    file_name,window_position = input_values()
    settings = iom.read_settings()
    data = iom.read_txt_file(file_name)
    driver = create_driver(settings)
    set_pyauto_settings()
    return driver,window_position,data,settings

def create_driver(settings: str, additional_options: list = []):
    options = webdriver.ChromeOptions()

    if additional_options:
        for add_option in additional_options:
            options.add_argument(add_option)

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-geolocation")
    prefs = {"profile.default_content_setting_values.geolocation" :2,
            "profile.default_content_setting_values.cookies": 2}
    
    options.add_experimental_option("prefs",prefs)  
    driver = webdriver.Chrome(
        executable_path = os.path.join(BASE_DIR, settings['pathes']['web_driver_path']),
        options = options
    )

    return driver

def set_pyauto_settings():
    pyautogui.PAUSE = 1.5
    pyautogui.FAILSAFE = True

def scroll_down(driver):
    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def input_values():
    file_name = input('Введите название файла: \n')
    window_position = input('Введите номер окна: \n')

    return file_name,window_position