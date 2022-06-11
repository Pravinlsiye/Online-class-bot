import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import schedule
import time
#from join import *
#from info import *
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })
#driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.chrome(executable_path="./chromedriver")
driver = webdriver.Chrome(chrome_options=opt,executable_path=r'/bin/chromedriver')
#class timing
firstClass = ("08:30")
secondClass = ("09:10")
thirdClass = ("09:50")
fourthClass = ("10:30")
fifthClass = ("11:15")
sixthClass = ("08:30")

#enter links here
english = ("https://")
maths = ("https://")
biology = ("https://")
physics = ("https://")
chemistry = ("https://")
dummy1 = ("https://meet.google.com/qrr-bhyt-jwb")

print("welcome")


def monday():
    schedule.every().monday.at(firstClass).do(joinEnglish())
    schedule.every().monday.at(secondClass).do(joinMaths())
    schedule.every().monday.at(thirdClass).do(joinBio())
    schedule.every().monday.at(fourthClass).do(joinPhysics())
    schedule.every().monday.at(fifthClass).do(joinChem())


def tuesday():
    schedule.every().tuesday.at(firstClass).do(joinPhysics())
    schedule.every().tuesday.at(secondClass).do(joinMaths())
    schedule.every().tuesday.at(thirdClass).do(joinBio())
    schedule.every().tuesday.at(fourthClass).do(joinChem())
    schedule.every().tuesday.at(fifthClass).do(joinEnglish())


def wednesday():
    schedule.every().wednesday.at(firstClass).do(joinEnglish())
    schedule.every().wednesday.at(secondClass).do(joinChem())
    schedule.every().wednesday.at(thirdClass).do(joinPhysics())
    schedule.every().wednesday.at(fourthClass).do(joinMaths())
    schedule.every().wednesday.at(fifthClass).do(joinMaths())


def thursday():
    schedule.every().thursday.at(firstClass).do(joinEnglish())
    schedule.every().thursday.at(secondClass).do(joinMaths())
    schedule.every().thursday.at(thirdClass).do(joinEnglish())
    schedule.every().thursday.at(fourthClass).do(joinChem())
    schedule.every().thursday.at(fifthClass).do(joinBio())


def friday():
    schedule.every().friday.at(firstClass).do(joinEnglish())
    schedule.every().friday.at(secondClass).do(joinChem())
    schedule.every().friday.at(thirdClass).do(joinPhysics())
    schedule.every().friday.at(fourthClass).do(joinMaths())
    schedule.every().friday.at(fifthClass).do(joinBio())


def sat():
    print("fun---sat")
    schedule.every().saturday.at(sixthClass).do(dummy())
    #schedule.every().saturday.at("12:15").do(dummy())
    

def joinEnglish():
    driver.get(english)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    googlelogin()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    print("--joining class--")
    time.sleep(10)
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/button/span')
    nextButton[0].click()
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div/button/span')
    nextButton[0].click()
    time.sleep(1800)
    driver.quit()

def joinPhysics():
    driver.get(physics)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    googlelogin()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    print("--joining class--Phy--")
    time.sleep(10)
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/button/span')
    nextButton[0].click()
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div/button/span')
    nextButton[0].click()
    time.sleep(1800)
    driver.quit()

def joinChem():
    driver.get(chemistry)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    googlelogin()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    print("--joining class--chem--")
    time.sleep(10)
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/button/span')
    nextButton[0].click()
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div/button/span')
    nextButton[0].click()
    time.sleep(1800)
    driver.quit()

def joinMaths():
    driver.get(maths)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    googlelogin()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    print("--joining class--math--")
    time.sleep(10)
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/button/span')
    nextButton[0].click()
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div/button/span')
    nextButton[0].click()
    time.sleep(1800)
    driver.quit()

def joinBio():
    driver.get(biology)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    googlelogin()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    print("--joining class--Bio--")
    time.sleep(10)
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/button/span')
    nextButton[0].click()
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div/button/span')
    nextButton[0].click()
    time.sleep(1800)
    driver.quit()

def dummy():
    driver.get(dummy1)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    googlelogin()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    print("--joining class--dummy")
    time.sleep(10)
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/div[3]/div[2]/div/div[2]/button/span')
    nextButton[0].click()
    nextButton = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div/button/span')
    nextButton[0].click()
    time.sleep(1800)
    driver.quit()
    
def googlelogin():
	print("running here")
	gmailId="pravinl.19cse@kongu.edu"
	passWord="Siye@2703"
	try:
    	   driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    	   driver.implicitly_wait(15)
  
    	   loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    	   loginBox.send_keys(gmailId)
  
    	   nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    	   nextButton[0].click()
  
    	   passWordBox = driver.find_element_by_xpath(
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    	   passWordBox.send_keys(passWord)
  
    	   nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    	   nextButton[0].click()
  
    	   print('Login Successful...!!')
    	   #time.sleep(100)
	except:
    	   print('Login Failed')
    	   
print("entering loop")
while True:
    schedule.run_pending()
    time.sleep(1)  # seconds
    e = datetime.datetime.now()
    print(e)
    day = (e.strftime("%a"))
    print(day)
    if day == "Mon":
    	monday()
    elif day == "Tue":
    	tuesday()
    elif day == "Wed":
    	wednesday()
    elif day == "Thu":
    	thursday()
    elif day == "Fri":
    	friday()
    elif day == "Sat":
    	print("--into sat---")
    	sat()
    else:
    	print("Its sunday bro")
