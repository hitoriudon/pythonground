from selenium import webdriver
from selenium.webdriver.common.keys import Keys #엔터쓸때
from selenium.webdriver import ActionChains #스크롤 다운
import discord

class PingPong(discord.Client):
    async def on_ready(self):
        print(f'Logged in as { self.user } (ID: { self.user.id })')
        await client.change_presence(activity=discord.Game(name='MT장소추천'))

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content == 'hi':
            ment1 = "👀 디스코드 MT장소 추천 봇\n\n'MT 장소? 내가 다 찾아줄께!'\n\n- 디스코드에서 사용가능한 한글 봇입니다.\n- 당신만을 위한 단 하나의 장소를 추천해드립니다! (조건에 부합하는 장소가 여러 곳일경우, 추천수가 가장 높은 장소를 선정했습니다)\n- '!'를 입력해 이용 메뉴얼을 확인해주세요"

            await message.reply(ment1, mention_author=False)

        if message.content == '!':
            ment1 = "📍명령방법\n-! : 봇 명령어 안내 링크를 보여줍니다.\n-!MT : 사용자가 입력한 조건 (지역, 인원수, 월, 일)에 맞춰 적합한 장소를 추천해줍니다.\n\n✔!MT 명령어 입력 방법\n=> !MT 지역 인원수 월 일 추가옵션 (EX : !MT 0 15 01 20 0,1,6)\n\n✔지역 입력 방법\n=> 하단의 선택지 중 원하시는 지역이 포함된 하나를 '숫자'를 골라 입력해주세요! (서울 내 지역 한정)\n\n🔍입력 가능 지역\n\n0. 강남/역삼/선릉/삼성\n1. 홍대/합정/상수\n2. 건대/구의/군자\n3. 영등포/문래/신길/대림\n4. 잠실/송파/방이\n5. 신촌/이대/아현/연희\n\n✔ 추가옵션 입력 방법\n=> 하단의 선택지 중 원하시는 옵션 여러개를 선택해 '숫자'를 입력해주세요!\n\n🔍 추가옵션\n\n0. TV/프로젝터\n1. 인터넷/WIFI\n2. 음향/마이크\n3. 음식물반입가능\n4. 주류반입가능\n5. 주차\n6. 금연\n7. 샤워시설"
            #ment3 = ment1
            await message.reply(ment1, mention_author=False)

        if message.content.startswith('!MT'):
            options = webdriver.ChromeOptions()
            options.add_argument('start-maximized')
            driver = webdriver.Chrome()
            driver.get('https://www.spacecloud.kr/search?q=%ED%8C%8C%ED%8B%B0%EB%A3%B8&page=1')
            
            b = message.content.split()
            loc = int(b[1])
            num = int(b[2])
            month = int(b[3])
            date = int(b[4])
            add0 = b[5]
            add1 = add0.split(',')
            add = []
            for i in add1:
                add.append(int(i))
            #r_value = {'location': int(loc), 'number': int(num),
            #          'month': int(month), 'date': int(date), 'add': add}
            
            driver.implicitly_wait(5)

            # 스페이스 클라우드 '파티룸' 접속

            driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(1) > button').click()
            driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(1) > div > ul > li:nth-child(1) > button').click()

            if loc==0: #강남/역삼/선릉/삼성
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(2) > button').click() #장소 버튼 클릭
            elif loc==1: #홍대/합정/상수
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(1) > div > ul > li.open > ul > li:nth-child(4) > button').click()
            elif loc==2: #건대/구의/군자
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(1) > div > ul > li.open > ul > li:nth-child(14) > button').click()
            elif loc==3: #영등포/문래/신길/대림
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(1) > div > ul > li.open > ul > li:nth-child(19) > button').click()
            elif loc==4: #잠실/송파/방이
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(1) > div > ul > li.open > ul > li:nth-child(25) > button').click()
            elif loc==5: #신촌/이대/아현/연희
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(1) > div > ul > li.open > ul > li:nth-child(5) > button').click()

            #인원 버튼 클릭
            driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(2) > button').click()
            for i in range(1, num): #인원수만큼 반복
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(2) > div > div.wrap-picker > div > button.btn-clear.btn-plus').click() #클릭클릭!

            driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(2) > div > button.btn-clear.btn-violet.filter').click() #인원 버튼 클릭
            driver.refresh() #새로고침 안 하면 인원 제한 잘 안 걸려서..

            #날짜 선택 
            driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > button').click() 
            for i in range (0,1): # 접으려고.. 한 것임
                if month==1 and date==16:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(1) > a').click()
                elif month==1 and date==17:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(2) > a').click()
                elif month==1 and date==18:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(3) > a').click()
                elif month==1 and date==19:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(4) > a').click()
                elif month==1 and date==20:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(5) > a').click()
                elif month==1 and date==21:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(6) > a').click()
                elif month==1 and date==22:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(7) > a').click()
                elif month==1 and date==23:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(5) > td:nth-child(1) > a').click()
                elif month==1 and date==24:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(5) > td:nth-child(2) > a').click()
                elif month==1 and date==25:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(5) > td:nth-child(3) > a').click()
                elif month==1 and date==26:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(5) > td:nth-child(4) > a').click()
                elif month==1 and date==27:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(5) > td:nth-child(5) > a').click()
                elif month==1 and date==28:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(5) > td:nth-child(6) > a').click()
                elif month==1 and date==29:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(5) > td:nth-child(7) > a').click()
                elif month==1 and date==30:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(6) > td:nth-child(1) > a').click()
                elif month==1 and date==31:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(6) > td:nth-child(2) > a').click()
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar_tit > a.btn_month_next > span').click()
                if month==2 and date==1:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(1) > td:nth-child(3) > a').click()
                elif month==2 and date==2:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(1) > td:nth-child(4) > a').click()
                elif month==2 and date==3:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(1) > td:nth-child(5) > a').click()
                elif month==2 and date==4:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(1) > td:nth-child(6) > a').click()
                elif month==2 and date==5:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(1) > td:nth-child(7) > a').click()
                elif month==2 and date==6:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(2) > td:nth-child(1) > a').click()
                elif month==2 and date==7:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(2) > td:nth-child(2) > a').click()
                elif month==2 and date==8:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(2) > td:nth-child(3) > a').click()
                elif month==2 and date==9:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(2) > td:nth-child(4) > a').click()
                elif month==2 and date==10:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(2) > td:nth-child(5) > a').click()
                elif month==2 and date==11:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(2) > td:nth-child(6) > a').click()
                elif month==2 and date==12:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(2) > td:nth-child(7) > a').click()
                elif month==2 and date==13:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(3) > td:nth-child(1) > a').click()
                elif month==2 and date==14:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(3) > td:nth-child(2) > a').click()
                elif month==2 and date==15:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(3) > td:nth-child(3) > a').click()
                elif month==2 and date==16:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(3) > td:nth-child(4) > a').click()
                elif month==2 and date==17:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(3) > td:nth-child(5) > a').click()
                elif month==2 and date==18:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(3) > td:nth-child(6) > a').click()
                elif month==2 and date==19:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(3) > td:nth-child(7) > a').click()
                elif month==2 and date==20:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(1) > a').click()
                elif month==2 and date==21:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(2) > a').click()
                elif month==2 and date==22:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(3) > a').click()
                elif month==2 and date==23:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(4) > a').click()
                elif month==2 and date==24:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(5) > a').click()
                elif month==2 and date==25:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(6) > a').click()
                elif month==2 and date==26:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(4) > td:nth-child(7) > a').click()
                elif month==2 and date==27:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(5) > td:nth-child(1) > a').click()
                elif month==2 and date==28:
                    driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > div.wrap-calendar > article > div.calendar > table > tbody > tr:nth-child(5) > td:nth-child(2) > a').click()
            #제출
            driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div:nth-child(3) > div > button.btn-clear.btn-violet.filter').click()

            # 옵션
            driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > button').click()
                
            if 0 in add: #tv/프로젝터
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > div > div.inner > div.wrap-filter.last > ul > li:nth-child(1) > label').click()
            if 1 in add: #WIFI
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > div > div.inner > div.wrap-filter.last > ul > li:nth-child(2) > label').click()
            if 2 in add: #음향/마이크
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > div > div.inner > div.wrap-filter.last > ul > li:nth-child(5) > label').click()
            if 3 in add: #음식물반입가능
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > div > div.inner > div.wrap-filter.last > ul > li:nth-child(7) > label').click()
            if 4 in add: #술반입가능
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > div > div.inner > div.wrap-filter.last > ul > li:nth-child(8) > label').click()
            if 5 in add: #주차
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > div > div.inner > div.wrap-filter.last > ul > li:nth-child(10) > label').click()
            if 6 in add: #금연 
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > div > div.inner > div.wrap-filter.last > ul > li:nth-child(11) > label').click()
            if 7 in add: #샤워시설
                driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > div > div.inner > div.wrap-filter.last > ul > li:nth-child(9) > label').click()
            #추가옵션 다 하고 제출버튼
            driver.find_element_by_css_selector('#__layout > div > div > div.content_wraper > div:nth-child(1) > div.search_wrap > div.btn_area > div > div > div.wrap-btn > button.btn-clear.btn-violet.filter').click()

            #가게 이름 모두 리스트에 저장
            names=driver.find_elements_by_class_name('tit_space')
            likes=driver.find_elements_by_class_name('txt_number_love')

            newlist=[]
            for i in range(len(names)):
                newlist.append(int(likes[i].text[4:]))
            #좋아요 가장 큰 값 반환
            knum=newlist.index(max(newlist))

            r_value=names[knum].text

            #디스코드 봇 응답
            await message.reply(r_value, mention_author=False) 


if __name__=='__main__':
    token_file = open('token', 'r')
    token = token_file.read()
    token_file.close()
    client = PingPong()
    client.run(token)