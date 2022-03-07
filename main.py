import datetime
from selenium import webdriver
import schedule
import time
from join import *
import info

driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\Desktop\classBot-chromedriver.exe")
e = datetime.datetime.now()


# timeTable.py combined in main.py to simplfy working

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


def dumm():
    schedule.every().saturday.at(dummyClass).do(dummy())


while True:
    schedule.run_pending()
    time.sleep(1)  # seconds

# Code for Timetable.py ends here

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
    dumm()
else:
    print("Its sunday bro")
