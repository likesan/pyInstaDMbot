

def insta_login(driver):
    driver.find_element_by_name('username').send_keys(id)
    driver.find_element_by_name('password').send_keys(pw)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/button/div').click()
    driver.implicitly_wait(4)

def if_alarm_asks_save_id_info(driver):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
    driver.implicitly_wait(0)

def if_alarm_set_ask_no(driver):
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button[2]').click()
    driver.implicitly_wait(0)