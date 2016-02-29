# -*- coding: utf-8 -*-
import sys
import time
import pyocr
import pyocr.builders
import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]

screen_path = '/tmp/screen.png'
code_path = '/tmp/code.png'
code_box = (826, 182, 889, 207)

# 重要
username = '******'
pwd = '********'

browser = webdriver.Firefox()
browser.implicitly_wait(10)


def crop_img(path, crop_path, box):
    """截图
    path: 图片地址
    crop_path: 剪贴地址
    box: 剪的坐标
    return: 无
    """
    im = Image.open(path)
    crop = im.crop(box)
    crop.save(crop_path)


def captcha_img_box():
    ele = browser.find_element_by_css_selector(
        '#captcha-img > img:nth-child(1)')
    return (ele.location['x'], ele.location['y'],
            ele.location['x'] + int(ele.get_attribute('width')),
            ele.location['y'] + int(ele.get_attribute('height')),
            )


def maybe_can_login():
    """
    返回验证码
    """
    while True:
        # http://selenium-python.readthedocs.org/waits.html
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#captcha-img"))
        )
        browser.get_screenshot_as_file(screen_path)
        crop_img(screen_path, code_path, captcha_img_box())
        code=tool.image_to_string(
            Image.open(code_path), lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        print(code)
        if len(code) == 4:
            return code
        browser.refresh()


def try_login(username, pwd, code):
    txt_username=browser.find_element_by_css_selector('.txt-username')
    txt_username.send_keys(username)
    txt_username.send_keys(Keys.RETURN)
    txt_pwd=browser.find_element_by_css_selector('.txt-password')
    txt_pwd.send_keys(pwd)
    txt_pwd.send_keys(Keys.RETURN)
    txt_captcha=browser.find_element_by_css_selector('.txt-captcha')
    txt_captcha.send_keys(code)
    txt_captcha.send_keys(Keys.RETURN)
    browser.find_element_by_css_selector('.btn-login').click()
    import time
    time.sleep(10)

    if u'\u767b\u5f55' not in browser.title:
        return True
    else:
        return False


def sign_and_getBeans():
    url='http://ld.m.jd.com/SignAndGetBeans/signStart.action'
    browser.get(url)
    time.sleep(60)

def main():
    url='http://m.jd.com/'
    browser.get(url)
    browser.find_element_by_css_selector('.jd-search-icon-login').click()
    try:
        while True:
            code=maybe_can_login()
            # 尝试login
            if try_login(username, pwd, code):
                sign_and_getBeans()
                break
            else:
                print("fail")

    finally:
        browser.quit()


if __name__ == '__main__':
    main()
