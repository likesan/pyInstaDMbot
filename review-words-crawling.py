import requests
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from selenium import webdriver as wd

tags = "#공구맘"
id = ''
pw = ''
insta_dm_page = 'https://www.instagram.com/direct/inbox/'
fit_influencers = []
influencers_size = 0
max = 50
avoid_block_sec = 15
like_cut = 1
# mkdir cookie folder
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-data-dir=selenium") 
driver = wd.Chrome('chromedriver.exe',chrome_options=chrome_options)
current_url = driver.current_url
actions = ActionChains(driver)

#def element(locator):
#   By = By.


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
    time.sleep(3)
    actions = ActionChains(driver)
    send_message_bttn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button')))
    actions.click(send_message_bttn).perform()
    print("[Clicked] the DM send button")

    input_id_on_dm_box = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')))
    actions.send_keys_to_element(input_id_on_dm_box, id_on_post_str)
    print("[Input] %s into ID input" ,id_on_post_str)



def search_good_gongumom(driver, insta_dm_page, current_url, actions):
    post = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div')))
    
    actions.move_to_element(post)
    actions.click(post).perform()
    driver.implicitly_wait(0.5)

    def next_pagination(driver, actions):
        time.sleep(avoid_block_sec)
        next_bttn = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/div/a[2]')))
        actions.click(next_bttn).perform()
        print("[Wait] " , avoid_block_sec , "sec")
# DM Sending proc needs this after

    while(len(fit_influencers) <= max) :
        try:
            post_likes_str = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/button/span'))).text 
            print("[Counted] Like Counts : " , post_likes_str) 
        
            #if the like counts are lower than 10, find next influencer's post
            if( int(post_likes_str) > like_cut ):
                print("[Counted] more than ", like_cut)
                id_on_post =  WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/a')))
                id_on_post_str = id_on_post.text
                print("[Added] ID : " + id_on_post_str)
                
                actions.click(id_on_post).perform()
                driver.get(insta_dm_page)
                
                dm_send(driver, id_on_post_str)
               
                fit_influencers.append(id_on_post_str)
                print('[Gathered] influencers ', fit_influencers)
                printf('[Counts] ', len(fit_influencers) ) 
                next_pagination(driver, actions)

            else:
                print("[Counted] less than ", like_cut)
                next_pagination(driver, actions)


        except NoSuchElementException:
                next_pagination(driver, actions)
        except TimeoutError:
            self.main()
 #       except ValueError:
  #              posts_likes = 
def main():
    open_insta_page(driver)
    #insta_login(driver)
    #if_alarm_asks_save_id_info(driver)
    #if_alarm_set_ask_no(driver)
    search_tag_to_input(driver, tags, current_url)
    search_good_gongumom(driver, insta_dm_page, current_url, actions)
    #driver.close()

if __name__ == "__main__":
    main()

