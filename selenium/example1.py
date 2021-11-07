from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Options는 생략 가능하다
options = webdriver.ChromeOptions()

# 창 크기 설정
#options.add_argument('window-size=1280,720')

# ...또는 창 최대화
options.add_argument('start-maximized')

# ...또는 헤드리스(창이 보이지 않는) 모드
#options.add_argument('--headless')
#options.add_argument('--disable-gpu') 
'''윈도우인 사람은 on, 아니면 off'''
 
# 드라이버 생성
driver = webdriver.Chrome()
#('chromedriver', options = options) '''이건 아무래도 윈도우 전용인 것 같다..'''

# 로딩 기다리기
driver.implicitly_wait(5)

# 구글 접속
driver.get('https://www.google.com')

# 검색창 찾기
#search = driver.find_element_by_name('q')
#search = driver.find_element_by_class_name('gLFyf') 
'''html class의 이름으로 찾을건데, 그 클래스의 이름은 gLFyf입니다. -> 근데 만약, 클래스 이름이 겹치면????'''
'''그래서 ! 셀렉터로 해결~~! '''
'''원본->''' #search = driver.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search = driver.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

# 검색어 입력
search.send_keys('한양대학교 포리프')

# 검색어 삭제
search.clear()

# 검색어 입력
search.send_keys('한양대학교 FORIF')

# 검색어 제출
#search.submit()

# 또는 엔터키 입력
search.send_keys(Keys.RETURN)

# 페이스북 링크 선택
facebook_link = driver.find_element_by_css_selector('#rso > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div.yuRUbf > a > h3')

# 링크 클릭
facebook_link.click()

# 뒤로 가기
driver.back() 

# 앞으로 가기
driver.forward() 

# 현재 주소 출력
print(driver.current_url)

# 드라이버 닫기
driver.quit()
