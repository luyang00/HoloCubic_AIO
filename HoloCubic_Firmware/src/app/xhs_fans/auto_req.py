# 
import appium
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
import time

def check_and_get_element_by_id(driver,resouce_id):
    try:
        element = driver.find_element(AppiumBy.ID, resouce_id)
        return element
    except:
        print('here:{}'.format(resouce_id))
        return None
def check_and_get_element_by_text(driver,text):
    try:
        element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(text) )
        return element
    except:
        print('here:{}'.format(text))
        return None
desired_caps = {
    'platformName':'Android',
    #用真机的时候，这个参数deviceName没什么用，但是还是必须要有这个参数，值的话随便填就行了
    'deviceName':'127.0.0.1:62001',
    'platformVersion':'7.1.2',
    'appPackage':'com.xingin.xhs',
    'appActivity':'.activity.SplashActivity',
    # 'unid':'127.0.0.1:62001',
    # 'noReset':'true',
    #  'adbPort':62001,
    # 'remoteAdbHost':'127.0.0.1'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
while True:
    agree_btn = check_and_get_element_by_id(driver,'com.xingin.xhs:id/cch')#同意按钮
    if agree_btn:
        agree_btn.click()
    
    login_via_phone_btn = check_and_get_element_by_id(driver,'com.xingin.xhs:id/cip')#手机登录
    if login_via_phone_btn:
        login_via_phone_btn.click()
        
        login_via_phone_pwd_btn = check_and_get_element_by_id(driver,'com.xingin.xhs:id/cn7')#手机密码登录
       
        while check_and_get_element_by_id(driver,'com.xingin.xhs:id/cn7') == None:
            pass
        check_and_get_element_by_id(driver,'com.xingin.xhs:id/cn7').click()

        while check_and_get_element_by_id(driver,'com.xingin.xhs:id/ciu') == None:
            pass
        
        account_id = check_and_get_element_by_id(driver,'com.xingin.xhs:id/cis')
        account_pwd = check_and_get_element_by_id(driver,'com.xingin.xhs:id/cjh')
        account_login_btn = check_and_get_element_by_id(driver,'com.xingin.xhs:id/ciu')
        if account_id and account_pwd and account_login_btn:
            account_id.send_keys('phone')
            account_pwd.send_keys('psd')
            account_login_btn.click()

    search_page_btn = check_and_get_element_by_id(driver,'com.xingin.xhs:id/e3e')#search button
    if search_page_btn:
        search_page_btn.click()
    if check_and_get_element_by_id(driver,'com.xingin.xhs:id/cmk'):
        search_input = check_and_get_element_by_id(driver,'com.xingin.xhs:id/cmk')#search input
        search_submit = check_and_get_element_by_id(driver,'com.xingin.xhs:id/cmo')
        if search_input and search_submit:
            search_input.send_keys('zhudayao')
            search_submit.click()
            while check_and_get_element_by_text(driver,'用户') == None:
                pass
            check_and_get_element_by_text(driver,'用户').click()

    if check_and_get_element_by_text(driver,'小红书号：zhudayao') and check_and_get_element_by_text(driver,'用户'):
        check_and_get_element_by_text(driver,'小红书号：zhudayao').click()
        time.sleep(5)
        check_and_get_element_by_id(driver,'com.xingin.xhs:id/dik').click()
        time.sleep(5)
            # driver.quit()    
#登录页
    #com.xingin.xhs:id/dal #其他登录方式
        #微博登录
    #com.xingin.xhs:id/ciq 手机号登录
        #com.xingin.xhs:id/cn7 手机密码登录
            #com.xingin.xhs:id/cis 手机号
            #com.xingin.xhs:id/cjh 密码
            #com.xingin.xhs:id/ciu 同意协议并登录
        #默认
            #com.xingin.xhs:id/cis 手机号
            #com.xingin.xhs:id/aaa请输入验证码
            #com.xingin.xhs:id/cnh 同意协议并登录
    #com.xingin.xhs:id/cip 上次登录

# time.sleep(3)
# driver.quit()