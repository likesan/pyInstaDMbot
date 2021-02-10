from selenium import webdriver 

from bs4 import BeautifulSoup 

from selenium.common.exceptions import NoSuchElementException        

import pandas as pd 

import time 

from datetime import datetime 

from selenium.webdriver.common.keys import Keys 

from selenium.webdriver.common.action_chains import ActionChains 

from selenium.webdriver.common.alert import Alert 

 

from selenium.common.exceptions import WebDriverException as WDE 

from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, ElementClickInterceptedException 

from selenium.webdriver.firefox.options import Options 

 

from requests.exceptions import ConnectionError 

from requests.packages.urllib3.exceptions import MaxRetryError 

from requests.packages.urllib3.exceptions import ProxyError as urllib3_ProxyError 

 

import random 

import pyperclip 

 

da = pd.read_excel('id_list.xlsx', 0) 

tcf = 0 

 

print("인스타그램 아이디 입력") 

ID = input() 

print("인스타그램 비밀번호 입력") 

Passwd = input() 

print("저장 파일이름 입력") 

file_name = input() 

 

### 해시태그, 크롤링 횟수, 팔로워수 기준 1씩 증가 

### 인스타그램 열기 

 

for i in range(len(da)) : 

 

    # chrome_options = webdriver.ChromeOptions() 

    # chrome_options.add_argument('headless') 

    # chrome_options.add_argument("--disable-gpu") 

    # chrome_options.add_argument("lang=ko_KR") 

 

    # chrome_options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36") 

    # , chrome_options=chrome_options 

     

     

    tag = da.loc[:,"해시태그"] 

    cawling_num = da.loc[:,"크롤링 횟수"] 

    follower_num = da.loc[:,"팔로워수 기준"] 

     

    print("해시태그", tag[tcf],"검색") 

    site_url = 'https://www.instagram.com/explore/tags/'+tag[tcf]+'/' 

         

    driver=webdriver.Chrome(executable_path='./chromedriver') 

    driver.get(site_url) 

    actions = ActionChains(driver) 

 

    influencer_name_df = pd.DataFrame(columns = ['ID']) 

 

#     ID = "abitogen_official" 

#     Passwd = "onrikorea02!" 

 

    md = 1 

    e = 0 

    e1 = 0 

    e2 = 0 

    te = 0 

 

    ### 로그인 

 

    for i in range(1) : 

        try :   

            time.sleep(3) 

            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click() 

 

            time.sleep(2) 

 

            driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(ID) 

            time.sleep(1) 

            driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Passwd) 

            time.sleep(1) 

            driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click() 

            time.sleep(3) 

            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click() 

            time.sleep(7) 

             

            c = 0 

            b = 0 

            while True : 

                if c == 10 : 

                    c = 1 

                 

                if b == 30 : 

                    break 

                     

                try : 

                    driver.find_element_by_xpath('/html/body/div[{}]/div/div/div/div[3]/button[2]'.format(c)).click() 

                    break 

                except NoSuchElementException : 

                    c += 1 

                    b += 1 

                    continue 

 

        except NoSuchElementException: 

            e += 1 

            print('error',e) 

            continue 

        except AttributeError : 

            e += 1 

            print('error',e) 

            continue 

        except ElementClickInterceptedException : 

            e += 1 

            print('error',e) 

            continue 

 

 

    ### 각각 게시글 클릭 

 

    a = 1 # 줄 바꾸기 

    b = 0 # 게시글 바꾸기 

     

    print(cawling_num[tcf],"회 크롤링") 

    for i in range(cawling_num[tcf]) : 

 

        if b == 3 : 

            a += 1 

            b = 1 

 

        else : 

            b += 1 

 

        for i in range(1) : 

            try : 

                time.sleep(1) 

                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[{}]/div[{}]/a/div/div[2]'.format(a, b)).click() 

                time.sleep(2) 

                html = driver.page_source 

                soup = BeautifulSoup(html,'html.parser') 

                influencer_name =soup.find_all('a', {'class':"_2dbep qNELH kIKUG"})[0] 

                influencer_name = influencer_name.find("img")["alt"] 

                influencer_name = influencer_name.split('님의')[0] 

                print(influencer_name) 

 

                click_num = random.randrange(1,5) 

    #             review_num = random.randrange(1,10) 

                share_num = random.randrange(1,5) 

    #             review = "ㅇㄷ" 

 

 

                if click_num < 3 : 

                    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div').click() 

                    time.sleep(1) 

 

 

                if share_num < 3 : 

                    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[1]/button').click() 

                    time.sleep(1) 

                    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/button[6]').click() 

 

                driver.find_element_by_xpath('/html/body/div[5]/div[3]/button/div').click() 

 

                influencer_name_bin = [] 

                influencer_name_bin.append(influencer_name) 

 

                influencer_name_zip = zip(influencer_name_bin) 

                for i in influencer_name_zip : 

                    influencer_name_c = i[0] 

                    influencer_name_df = influencer_name_df.append(pd.DataFrame([[influencer_name_c]], columns=['ID'])) 

                    influencer_name_df.drop_duplicates(subset="ID",keep="first",inplace=True) 

 

            except NoSuchElementException: 

                e1 += 1 

                print('error 1-1',e1) 

                continue 

            except AttributeError : 

                e1 += 1 

                print('error 1-2',e1) 

                continue 

            except ElementClickInterceptedException : 

                e1 += 1 

                print('error 1-3',e1) 

                continue 

 

            except NameError : 

                e1 += 1 

                print('error 1-4',e1) 

                continue    

 

            finally : 

                if 5 < e1 : 

                    try : 

                        driver.find_element_by_xpath('/html/body/div[5]/div[3]/button/div').click() 

                        time.sleep(1) 

                    except NoSuchElementException: 

                        print('error 1-1') 

                        pass 

                    except AttributeError : 

                        print('error 1-1') 

                        pass 

                    except ElementClickInterceptedException : 

                        print('error 1-1') 

                        pass 

                    except NameError : 

                        print('error 1-4') 

                        pass 

 

                    time.sleep(1) 

                    driver.refresh()        

                    time.sleep(3) 

 

    driver.quit()  

 

 

    influencer_info_df = pd.DataFrame(columns = ['ID','포스트','팔로워','팔로우','라이브포스트 반응','URL']) 

 

 

    # chrome_options = webdriver.ChromeOptions() 

    # chrome_options.add_argument('headless') 

    # chrome_options.add_argument("--disable-gpu") 

    # chrome_options.add_argument("lang=ko_KR") 

 

    # chrome_options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36") 

    # , chrome_options=chrome_options 

 

 

    site_url = 'http://influencer.mediance.co.kr/analytics/instagram/abitogen_official' 

    driver = webdriver.Chrome(executable_path='./chromedriver') 

    driver.get(site_url) 

    time.sleep(1) 

 

    for i in range(len(influencer_name_df)) : 

 

        a = influencer_name_df.iloc[i, : ] 

 

        for i in a : 

            influencer_ID = i 

 

            driver.find_element_by_xpath('//*[@id="cm_name"]').send_keys(influencer_ID) 

            time.sleep(1) 

            driver.find_element_by_xpath('//*[@id="btn_tag_search"]').send_keys(Keys.ENTER) 

            time.sleep(3) 

 

            while True : 

                te += 1 

 

                print("True erro :", te) 

 

                if 10 < te : 

                    driver.refresh() 

                    time.sleep(3) 

                    te = 0 

 

                else : 

                    try : 

                        influencer_post_num = driver.find_element_by_xpath('//*[@id="wrap_search_tag"]/div[2]/div/div[2]/div/div[2]/ul/li[1]/span[2]') 

                        influencer_follower_num = driver.find_element_by_xpath('//*[@id="wrap_search_tag"]/div[2]/div/div[2]/div/div[2]/ul/li[2]/span[2]') 

                        influencer_follow_num = driver.find_element_by_xpath('//*[@id="wrap_search_tag"]/div[2]/div/div[2]/div/div[2]/ul/li[3]/span[2]') 

                        influencer_Livepost_reactionrate = driver.find_element_by_xpath('//*[@id="wrap_search_tag"]/div[4]/div/div[2]/div[1]/div/div[1]/span/span/b') 

                        influencer_URL = 'www.instagram.com/' + influencer_ID + '/' 

 

                        influencer_post_num = influencer_post_num.text 

 

                        try : 

                            int_influencer_post_num = influencer_post_num.replace(',','') 

                            int_influencer_post_num = int(int_influencer_post_num) 

                        except ValueError : 

                            int_influencer_post_num = 0 

                            pass                    

 

 

                        influencer_follower_num = influencer_follower_num.text 

 

                        try : 

                            int_influencer_follower_num = influencer_follower_num.replace(',','') 

                            int_influencer_follower_num = int(int_influencer_follower_num) 

                        except ValueError : 

                            int_influencer_follower_num = 0 

                            pass    

 

 

                        influencer_follow_num = influencer_follow_num.text 

 

                        try : 

                            int_influencer_follow_num = influencer_follow_num.replace(',','') 

                            int_influencer_follow_num = int(int_influencer_follow_num) 

                        except ValueError : 

                            int_influencer_follow_num = 0 

                            pass    

 

                        influencer_Livepost_reactionrate = influencer_Livepost_reactionrate.text 

 

                        try : 

                            int_influencer_Livepost_reactionrate = float(influencer_Livepost_reactionrate) 

                        except ValueError : 

                            int_influencer_Livepost_reactionrate = 0 

                            pass    

 

                        influencer_ID_bin = [] 

                        influencer_ID_bin.append(influencer_ID) 

 

                        influencer_post_num_bin = [] 

                        influencer_post_num_bin.append(int_influencer_post_num) 

 

                        influencer_follower_num_bin = [] 

                        influencer_follower_num_bin.append(int_influencer_follower_num) 

 

                        influencer_follow_num_bin = [] 

                        influencer_follow_num_bin.append(int_influencer_follow_num) 

 

                        influencer_Livepost_reactionrate_bin = [] 

                        influencer_Livepost_reactionrate_bin.append(int_influencer_Livepost_reactionrate) 

 

                        influencer_URL_bin = [] 

                        influencer_URL_bin.append(influencer_URL) 

 

 

                        print(md,'명 검색') 

                        md += 1 

 

                        te = 0 

 

                        influencer_info_zip = zip(influencer_ID_bin,influencer_post_num_bin,influencer_follower_num_bin,influencer_follow_num_bin,influencer_Livepost_reactionrate_bin,influencer_URL_bin) 

                        for i in influencer_info_zip : 

                            influencer_ID_c = i[0] 

                            influencer_post_num_c = i[1] 

                            influencer_follower_num_c = i[2] 

                            influencer_follow_num_c = i[3] 

                            influencer_Livepost_reactionrate_c = i[4] 

                            influencer_URL_c = i[5] 

                            influencer_info_df = influencer_info_df.append(pd.DataFrame([[influencer_ID_c,influencer_post_num_c,influencer_follower_num_c,influencer_follow_num_c,influencer_Livepost_reactionrate_c,influencer_URL_c]], columns=['ID','포스트','팔로워','팔로우','라이브포스트 반응','URL'])) 

                    except UnexpectedAlertPresentException : 

                        print("UnexpectedAlertPresentException") 

                        continue 

                    except NoSuchElementException : 

                        print("NoSuchElementException") 

                        continue 

                break 

 

    driver.quit() 

 

    ### 검색 조건 걸기 

     

    print("팔로워 수",follower_num[tcf],"이상 선택") 

    int_influencer_info_df = pd.DataFrame(influencer_info_df) 

    df_int_influencer_info_df = int_influencer_info_df['팔로워'] > follower_num[tcf] 

    filtered_df = int_influencer_info_df[df_int_influencer_info_df]         

 

    print(filtered_df) 

     

    filtered_df.to_excel('./파일/{}.xlsx'.format(file_name)) 
