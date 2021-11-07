import sys
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

# 파일에서 ID, 비밀번호 읽기
id_file = open('id', 'r')
pw_file = open('pw', 'r')

id_str = id_file.read()
pw_str = pw_file.read()

id_file.close()
pw_file.close()

# 웹 드라이버 옵션 만들기
options = webdriver.ChromeOptions()

#options.add_argument('start-maximized')
options.add_argument('--headless')
#options.add_argument('--disable-gpu') 

# 웹 드라이버 만들기
driver = webdriver.Chrome() #수정햇어여
driver.implicitly_wait(10)

# LMS 사이트 접속하기
driver.get('http://learning.hanyang.ac.kr')

# 로그인 하기 ''' 크롬 검사 두 번 눌러서.. 아이디 값을 복사해서.. 그런 느낌이예요 확실히 검사를 진짜 많이 쓰긴 하겠당'''
id_box = driver.find_element_by_id('uid')
pw_box = driver.find_element_by_id('upw')
login  = driver.find_element_by_id('login_btn')

id_box.send_keys(id_str)
pw_box.send_keys(pw_str)
login.click()

try:
    alert = Alert(driver)

    # 비밀번호를 바꾸라는 경고
    if alert.text.startswith('한양대학교 포털 한양인에서는 회원님의 개인정보를 안전하게 보호하고'):
        alert.accept()
    # 아이디 혹은 비밀번호가 틀렸을 때
    else:
        alert.accept()
        print('아이디 혹은 비밀번호가 틀렸습니다.')
        sys.exit()
except:
    pass

# 과목들 가져오기 
''' 과목들을 가져오고 싶은데, 과목이 한 개가 아니니까 과목 html 검사해서 공통적인 class든 id든 찾아야함. 그게 바로 밑에 줄 코드!'''
classes = driver.find_elements_by_class_name('ic-DashboardCard__header-subtitle')

# 과목들 출력
for cs in classes:
    print(cs.text)
 
# 웹 드라이버 종료
driver.quit()
'''푸시가 가장 어려운 것 같다'''