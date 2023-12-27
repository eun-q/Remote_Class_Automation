import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

id = 'your id'
passward = 'your passward'
class1 = 'class' # 내가 수강하는 과목의 아이디

# 크롬
path = '/chromedriver'
driver = webdriver.Chrome(path)
# 사이트 접속
driver.get('') # 접속이 필요한 홈페이지 주소
driver.set_window_size(1920, 1080) # 불러올 때 화면 사이즈 변환

# 아이디 textfield 선택
driver.find_element(By.XPATH, '//*[@id="login"]/input[1]').click()
# 아이디 입력
pyautogui.typewrite(id)
# 비번 클릭
driver.find_element(By.XPATH, '//*[@id="login"]/input[2]').click()
# 비번 입력
pyautogui.typewrite(passward)
# 로그인 버튼 선택
driver.find_element(By.XPATH, '//*[@id="login"]/button').click()

# 내 강의실
driver.find_element(By.XPATH, '//*[@id="main_contents"]/ul[1]/li[1]/ul/li[1]').click()
# 수업 아이디
driver.find_element(By.XPATH, class1).click()
# 수강하기 진입
driver.find_element(By.XPATH, '//*[@id="contentsArea"]/ul/li[2]/form/table/tbody/tr[1]/td[4]/button').click()
driver.switch_to.window(driver.window_handles[1]) # 팝업 전환
# 해당 부분에 비디오 플레이어로 진입하는 동작 필요
# 그래야 비디오 플레이어 안의 요소들을 컨트롤 할 수 있다.
next_balloon = driver.find_element(By.XPATH, '//*[@id="balloonUI"]/button')
el2 = driver.find_element(By.XPATH, '//*[@id="next"]')

for i in range(1, 100):
    try:
        # 최대 600초 동안 대기
        wait = WebDriverWait(driver, 600)

        # balloonUI 요소의 button 하위 요소가 나타날 때까지 대기
        button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="balloonUI"]/button')))
        print("풍선 발견 대기 종료")
        time.sleep(5)

        # button 요소를 클릭
        button.click()
        print("풍선 선택")
    except Exception as e:
        pass
        print("풍선없음 패스", e)