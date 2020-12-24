import requests
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

# mkdir cookie folder
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-data-dir=selenium") 
driver = wd.Chrome('chromedriver.exe',chrome_options=chrome_options)
current_url = driver.current_url

def open_insta_page(driver):
    url = 'https://www.instagram.com/'
    driver.get(url)
    driver.implicitly_wait(5)

# first-login

# first-login line end

def search_tag_to_input(driver, tags, current_url):
    input_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    input_box.send_keys(tags)
    driver.implicitly_wait(3)
    first_tab_hashtag = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')))
    first_tab_hashtag.click()
    # driver.implicitly_wait(4)
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))

def search_good_gongumom(driver, insta_dm_page):
    post = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div')))
    
    actions = ActionChains(driver)
    actions.move_to_element(post)
    actions.click(post).perform()
    driver.implicitly_wait(0.5)

    def next_pagination(driver, actions):
        next_bttn = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div/div/a[2]')))
        actions.click(next_bttn).perform()
        driver.implicitly_wait(3.5)

    while(len(fit_influencers) <= max) :
        try:
            post_likes = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/button/span'))).text 
            print("좋아요 수 : " + post_likes)
            
            #if the like counts are lower than 40, find next influencer's post
            if( int(post_likes) > 40 ):
                print("40보다 크므로 GET")
                id_on_post = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/a').text
                
                print("아이디 : " + id_on_post)
                
                fit_influencers.append(id_on_post)
                print(fit_influencers, len(fit_influencers))
                next_pagination(driver, actions)

# DM Sending proc needs this after

            else:
                print("40보다 작으므로 다음")
                next_pagination(driver, actions)


        except NoSuchElementException:
                next_pagination(driver, actions)
        except TimeoutError:
                open_insta_page(driver)
                search_tag_to_input(driver,tags,current_url)
                search_good_gongumom(driver, insta_dm_page)


open_insta_page(driver)
#insta_login(driver)
#if_alarm_asks_save_id_info(driver)
#if_alarm_set_ask_no(driver)
search_tag_to_input(driver, tags, current_url)
search_good_gongumom(driver, insta_dm_page)
#driver.close()
