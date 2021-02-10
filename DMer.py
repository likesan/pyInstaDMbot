from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time
import schedule

x = 0

def login(browser, username, password):

    usrname_bar = browser.find_element_by_name('username')
    passwrd_bar = browser.find_element_by_name('password')

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    time.sleep(11)


def dmer():
    global x
    
    account_selection = input("""

Select which ID will you operate?

1. therabrain_marketing
2. thera_brain
3. therabrain
4. therabrain___


> """)

    usrnames = [
            'hanamam_heesoo', 'imira586'
            ]
    browser_options = Options()
    browser_options.add_argument("--disable-dev-shm-usage"); 
 
    if( account_selection == '1'):
        username = 'therabrain_marketing'  # Enter your username here
        password = 'onrikorea00!'  # Enter your password here
    elif( account_selection == '2'):
        username = 'thera_brain' 
        password = 'onrikorea00!'
    elif( account_selection == '3'):
        username = 'therabrain'
        password = 'Onrikorea00!'
    elif( account_selection == '4'):
        username = 'therabrain___'
        password = 'onrikorea00!'
    
    print(f'login through {username}')
    browser_options.add_argument(f"user-data-dir={username}") 
    browser_options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    browser = webdriver.Chrome("chromedriver.exe", options=browser_options)
    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    if('login' in browser.current_url):
        login(browser, username, password) 


    def send_msg(usrnames):
        # 전교 1등의 경우 
        gongu_msg = f"""
        
안녕하세요! {usrnamee}님

온누리아이코리아 연세테라브레인 공동구매 진행 담당자 윤승진이라고 합니다 : )

연세테라브레인은 기억력개선 영양제 부문 판매 1위 달성, 출시 3달만에 기억력, 집중력 영양제 부문 판매1위 달성한 제품입니다.

{usrnamee}님이 진행하시면 좋은 호응을 얻을 수 있을거라 생각합니다.

공구 진행 시 구매건당 최대 30,000원의 커미션과 65,000원 상당 제품 제안 드립니다.

■ 제품 : 연세테라브레인 1 통 / 1 박스/ 2 박스
■ 모든 옵션 구매시 6포 체험분 제공, 12일 이내 100% 환불 보장
■ 커미션 : 10,000 / 15,000 / 30,000
■ 공구가 : 49,900 / 78,000 / 150,000
■ 최소판매량 없음!!!

연세테라브레인이란 연세대학교에서 만들어 식품의약품안전처, 4개국 특허받은 신뢰성 있는 제품입니다.

공동구매에 관심이 있으시다면 위쪽에 첨부한 구글폼에 양식 작성 부탁 드립니다.

※ 구글폼 최상단에 위치한 [ 공동구매 안내 ] 글을 꼭 확인 부탁드립니다.
※ 커미션 지급 시 3.3% 원천징수가 진행 됩니다.


"""
        

        gongu_abtg_msg = f"""
        
안녕하세요! {usrnamee}님

온누리아이코리아 연세테라브레인 공동구매 진행 담당자 윤승진이라고 합니다 : )

지난번 아비토젠 공동구매 진행 정말 잘 진행해주셔서요!

이번에 다른 제품도 공동구매 진행을 부탁드리기 위해 DM 드립니다.

연세테라브레인은 기억력개선 영양제 부문 판매 1위 달성, 출시 3달만에 기억력, 집중력 영양제 부문 판매1위 달성한 제품입니다.

{usrnamee}님이 진행하시면 좋은 호응을 얻을 수 있을거라 생각합니다.

공구 진행 시 구매건당 최대 30,000원의 커미션과 65,000원 상당 제품 제안 드립니다.

■ 제품 : 연세테라브레인 1 통 / 1 박스/ 2 박스
■ 모든 옵션 구매시 6포 체험분 제공, 12일 이내 100% 환불 보장
■ 커미션 : 10,000 / 15,000 / 30,000
■ 공구가 : 49,900 / 78,000 / 150,000
■ 최소판매량 없음!!!

연세테라브레인이란 연세대학교에서 만들어 식품의약품안전처, 4개국 특허받은 신뢰성 있는 제품입니다.

공동구매에 관심이 있으시다면 위쪽에 첨부한 구글폼에 양식 작성 부탁 드립니다.

※ 구글폼 최상단에 위치한 [ 공동구매 안내 ] 글을 꼭 확인 부탁드립니다.
※ 커미션 지급 시 3.3% 원천징수가 진행 됩니다.


"""
        browser.get('https://www.instagram.com/direct/new/')

        time.sleep(5)

        to_btn = browser.find_element_by_name('queryBox')
        to_btn.send_keys(usrnames)

        time.sleep(8)

        chk_mrk = browser.find_element_by_class_name('dCJp8')
        chk_mrk.click()

        time.sleep(3)

        nxt_btn = browser.find_element_by_xpath('//div[@class="mXkkY KDuQp"]')
        nxt_btn.click()

        time.sleep(6)

        browser.execute_script("""
                var element = document.querySelector(".vohlx");
                if (element)
                    element.parentNode.removeChild(element);
        """)


        txt_box = browser.find_element_by_tag_name('textarea')

        # 공구 진행 신청서
        txt_box.send_keys("https://bit.ly/3nh4RLK")
        time.sleep(1)

        snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
        snd_btnn = snd_btn[len(snd_btn)-1]
        snd_btnn.click()
        

        # 공구 진행 요청
        txt_box.send_keys(gongu_msg)  # Customize your message
        

        time.sleep(1)

        snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
        snd_btnn = snd_btn[len(snd_btn)-1]
        snd_btnn.click()
        
        print(f"sent DM to {usrnamee}")

        time.sleep(4)

    count = 1
    try:
        for usrnamee in usrnames:
            send_msg(usrnamee)
            count += 1
            if(count==5):
                an_hour = 3600
                print(f"Sleep after {an_hour} sec")
                time.sleep(an_hour)
            elif(count%2==0):
                send_msg("___sj___y")

    except TypeError:
        print('Failed!')

    browser.quit()

    print(f'''
    Successfully Sent {count} Massages
    ''')

    x += 1



try:
    print("On at :", datetime.now().time())
    dmer()
except TypeError:
    pass
except NoSuchElementException:
    print(f"Sleep 3600 sec")
    time.sleep(3600)
    pass
# except 더 이상 보내지 못하는 경우 ... ?


try:
    while True and x != 1:
        schedule.run_pending()
        time.sleep(1)
except UnboundLocalError:
    pass
