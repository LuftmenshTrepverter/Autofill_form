from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time
from selenium.webdriver.common.keys import Keys


# 问卷自动填写：
def auto():
    driver = webdriver.Chrome('chromedriver.exe')
    wait = WebDriverWait(driver, 30)
    driver.get("https://XXX")  # 问卷网址

    # 姓名
    name_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div[1]/div/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/span/span/input')))
    sid_input.clear()
    name_input.send_keys('XXX')  # 在这写入你的姓名

    # 学号
    sid_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div[1]/div/form/div[3]/div[1]/div[4]/div/div/div[2]/div[1]/div/span/input')))
    sid_input.clear()
    sid_input.send_keys('XXXXXX')  # 在这写入你的学号

    # 学生类型:全日制
    scholName = wait.until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div/div[1]/div/form/div[3]/div[1]/div[6]/div/div[2]/div/div/span/div/div[1]/div/div/label')))  # FRjZ代表清水河校区，如果是沙河的话，这里把FRjZ换成1FRN
    scholName.click()

    # 住宿地点：校内
    scholName = wait.until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div/div[1]/div/form/div[3]/div[1]/div[8]/div/div[2]/div/div/span/div/div[1]/div/div/label/span[2]/span')))  # FRjZ代表清水河校区，如果是沙河的话，这里把FRjZ换成1FRN
    scholName.click()

    # 选择校区：清水河
    scholName = wait.until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div/div[1]/div/form/div[3]/div[1]/div[10]/div/div[2]/div/div/span/div/div[1]/div/div/label/span[2]/span')))  # FRjZ代表清水河校区，如果是沙河的话，这里把FRjZ换成1FRN
    scholName.click()

    # 选择是否在11点之前回寝：是
    goHome = wait.until(EC.presence_of_element_located((By.XPATH,
                                                        '/html/body/div/div[1]/div/form/div[3]/div[1]/div[12]/div/div[2]/div/div/span/div/div[1]/div/div/label/span[2]/span')))  # 11点前回寝就用VH1i，否则用S7oT
    goHome.click()

    #获取地理位置
    position = wait.until(EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="root"]/div/form/div[3]/div[1]/div[14]/div/div/div[2]/div/div/span/div/div/button')))

    position.click()
    time.sleep(10)

    # 提交
    submit = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/form/div[5]/div/button')))
    submit.click()
    #
    # # 关闭网页
    driver.quit()


# 定时功能：
schedule.every().day.at("XX:XX").do(auto)  # 这里改成你想自动提交的时间

while True:
    schedule.run_pending()
    #time.sleep(30)