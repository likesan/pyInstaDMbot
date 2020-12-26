import requests
import re
import time 
import traceback
import xlwt 
from xlwt import Workbook 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver as wd

tags = "#공구맘"
id = ''
pw = ''
insta_dm_page = 'https://www.instagram.com/direct/inbox/'
fit_influencers = []
influencers_size = 0
max = 50
avoid_block_sec = 3
like_cut = 1
# mkdir cookie folder
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-data-dir=selenium") 
chrome_options.add_argument("--disable-dev-shm-usage")
driver = wd.Chrome('chromedriver.exe',chrome_options=chrome_options)
current_url = driver.current_url
actions = ActionChains(driver)


def open_insta_page(driver):
    url = 'https://www.instagram.com/'
    driver.get(url)
    driver.implicitly_wait(5)

def search_tag_to_input(driver, tags, current_url):
    input_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    input_box.send_keys(tags)
    driver.implicitly_wait(3)
    first_tab_hashtag = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')))
    first_tab_hashtag.click()
    # driver.implicitly_wait(4)
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))

def dm_send(driver, id_on_post_str):
    driver.get(insta_dm_page)
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))
    time.sleep(3)
    actions = ActionChains(driver)

    send_message_bttn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button[text()="메시지 보내기"]')))
    actions.send_keys_to_element(send_message_bttn, Keys.ENTER).perform()
    print("[clicked] the dm send button")
    time.sleep(1.5)

    #input scrapped ID into the '받는사람'
    input_id_on_dm_box = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.NAME, 'queryBox')))
    actions.send_keys_to_element(input_id_on_dm_box, id_on_post_str).perform()
    print("[Input] into ID input ", id_on_post_str)

    time.sleep(4.5)
    
    #click the radio button
    radio_bttn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button/span')))
    actions.click(radio_bttn).perform()
    print("[clicked] the Radio button")

    time.sleep(4.5)
    # #click next
    next_bttn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button')))
    actions.click(next_bttn).perform()



def next_pagination(driver):
    actions = ActionChains(driver)
    time.sleep(avoid_block_sec)
    next_bttn = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/div/a[2]')))
    actions.click(next_bttn).perform()
    print("[Wait] " , avoid_block_sec , "sec")

def scappying_post_likes(driver):
    try:
        post_likes_str = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/button/span'))).text 
    except Exception as e:
        stacktrace = traceback.format_exc()
        if 'post_likes_str' in stacktrace:
            next_pagination(driver)
        print("[Counted] Like Counts : " , post_likes_str) 

def check_number_of_followers(driver, fit_influencers, id_on_post_str):
    follower_counts_str = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'))).text
    if ',' in follower_counts_str:
        follower_counts_str = follower_counts_str.replace(',','')
        print('[Is removed]' , follower_counts_str)
    if int(follower_counts_str) > 1000:
        fit_influencers.append(id_on_post_Str) 

def search_good_gongumom(driver, insta_dm_page, current_url):
    actions = ActionChains(driver)
    post = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div')))
    actions.move_to_element(post).perform()
    actions.click(post).perform()

# while loop need to be added

    id_on_post =  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/a')))
    id_on_post_str = id_on_post.text
    fit_influencers.append(id_on_post_str)
    print("[Added] ID : " + id_on_post_str)
    # actions.click(id_on_post).perform()
    # check_number_of_followers(driver, fit_influencers, id_on_post_str)
    # add all id into excel or some other place.
    wb = Workbook()
    sheet1 = wb.add_sheet('insta_gongu_mom_list')

    sheet1.write(0, 0, 'Instagram ID')
    first_x_row = 1;
    sheet1.write(1, 0, id_on_post_str)
    wb.save('insta_gongu.xls')

    # dm_send(driver, id_on_post_str)
    
    print('[Gathered] influencers ', fit_influencers)
    print('[Gathered Influencers] ', len(fit_influencers) ) 
    next_pagination(driver)



def main():
    open_insta_page(driver)
    search_tag_to_input(driver, tags, current_url)
    search_good_gongumom(driver, insta_dm_page, current_url)
    
if __name__ == "__main__":
    try:
        main()
        driver.close()
    except Exception as e:
        stacktrace = traceback.format_exc()
        print(stacktrace)
        

