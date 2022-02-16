import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import schedule
import scheduler as s
import subprocess
from sub import c_green, c_red, c_blue, c_white, c_yellow

# Vars:
PATH = './geckodriver.exe'
ID = s.Zoom_Room


def job():
    try:
        service = Service(PATH)
        options = FirefoxOptions()
        options.headless = True
        profile = "./Profile"
        options.profile = profile
        driver = webdriver.Firefox(options=options, service=service)
        driver.get(f"https://zoom.us/j/{ID}")
        watch = time.strftime("%H:%M - %d/%m/%y")
        print(f"{c_white}[{watch}] {c_green}Joined Zoom Room {ID}{c_white}\n")
        file = open(r"./logger.txt", "a")
        file.write(f"[{watch}] Joined Zoom Room {ID}\n")
        time.sleep(2)
        driver.quit()
    except:
        watch = time.strftime("%H:%M - %d/%m/%y")
        print(f"{c_white}[{watch}] {c_red}Something went wrong!{c_white}\n")
        file = open(r"./logger.txt", "a")
        file.write(f"[{watch}] Something went wrong!\n")


def killzoom():
    DETACHED_PROCESS = 0x00000008
    subprocess.call('taskkill /F /IM Zoom.exe /FI "WindowTitle eq Zoom Meeting" /T', creationflags=DETACHED_PROCESS)
    time.sleep(7)
    subprocess.call('taskkill /F /IM Zoom.exe /FI "WindowTitle eq Zoom Meeting" /T', creationflags=DETACHED_PROCESS)


# Schedule Sun:
try:
    schedule.every().sunday.at(s.Sun1).do(job)
except:
    pass
try:
    schedule.every().sunday.at(s.SunK1).do(killzoom)
except:
    pass
try:
    schedule.every().sunday.at(s.Sun2).do(job)
except:
    pass
try:
    schedule.every().sunday.at(s.SunK2).do(killzoom)
except:
    pass
try:
    schedule.every().sunday.at(s.Sun3).do(job)
except:
    pass
try:
    schedule.every().sunday.at(s.SunK3).do(killzoom)
except:
    pass
try:
    schedule.every().sunday.at(s.Sun4).do(job)
except:
    pass
try:
    schedule.every().sunday.at(s.SunK4).do(killzoom)
except:
    pass
try:
    schedule.every().sunday.at(s.Sun5).do(job)
except:
    pass
try:
    schedule.every().sunday.at(s.SunK5).do(killzoom)
except:
    pass
try:
    schedule.every().sunday.at(s.Sun6).do(job)
except:
    pass
try:
    schedule.every().sunday.at(s.SunK6).do(killzoom)
except:
    pass
try:
    schedule.every().sunday.at(s.Sun7).do(job)
except:
    pass
try:
    schedule.every().sunday.at(s.SunK7).do(killzoom)
except:
    pass
# Schedule Mon:
try:
    schedule.every().monday.at(s.Mon1).do(job)
except:
    pass
try:
    schedule.every().monday.at(s.MonK1).do(killzoom)
except:
    pass
try:
    schedule.every().monday.at(s.Mon2).do(job)
except:
    pass
try:
    schedule.every().monday.at(s.MonK2).do(killzoom)
except:
    pass
try:
    schedule.every().monday.at(s.Mon3).do(job)
except:
    pass
try:
    schedule.every().monday.at(s.MonK3).do(killzoom)
except:
    pass
try:
    schedule.every().monday.at(s.Mon4).do(job)
except:
    pass
try:
    schedule.every().monday.at(s.MonK4).do(killzoom)
except:
    pass
try:
    schedule.every().monday.at(s.Mon5).do(job)
except:
    pass
try:
    schedule.every().monday.at(s.MonK5).do(killzoom)
except:
    pass
try:
    schedule.every().monday.at(s.Mon6).do(job)
except:
    pass
try:
    schedule.every().monday.at(s.MonK6).do(killzoom)
except:
    pass
try:
    schedule.every().monday.at(s.Mon7).do(job)
except:
    pass
try:
    schedule.every().monday.at(s.MonK7).do(killzoom)
except:
    pass
# Schedule Tues:
try:
    schedule.every().tuesday.at(s.Tue1).do(job)
except:
    pass
try:
    schedule.every().tuesday.at(s.TueK1).do(killzoom)
except:
    pass
try:
    schedule.every().tuesday.at(s.Tue2).do(job)
except:
    pass
try:
    schedule.every().tuesday.at(s.TueK2).do(killzoom)
except:
    pass
try:
    schedule.every().tuesday.at(s.Tue3).do(job)
except:
    pass
try:
    schedule.every().tuesday.at(s.TueK3).do(killzoom)
except:
    pass
try:
    schedule.every().tuesday.at(s.Tue4).do(job)
except:
    pass
try:
    schedule.every().tuesday.at(s.TueK4).do(killzoom)
except:
    pass
try:
    schedule.every().tuesday.at(s.Tue5).do(job)
except:
    pass
try:
    schedule.every().tuesday.at(s.TueK5).do(killzoom)
except:
    pass
try:
    schedule.every().tuesday.at(s.Tue6).do(job)
except:
    pass
try:
    schedule.every().tuesday.at(s.TueK6).do(killzoom)
except:
    pass
try:
    schedule.every().tuesday.at(s.Tue7).do(job)
except:
    pass
try:
    schedule.every().tuesday.at(s.TueK7).do(killzoom)
except:
    pass
# Schedule Wed:
try:
    schedule.every().wednesday.at(s.Wed1).do(job)
except:
    pass
try:
    schedule.every().wednesday.at(s.WedK1).do(killzoom)
except:
    pass
try:
    schedule.every().wednesday.at(s.Wed2).do(job)
except:
    pass
try:
    schedule.every().wednesday.at(s.WedK2).do(killzoom)
except:
    pass
try:
    schedule.every().wednesday.at(s.Wed3).do(job)
except:
    pass
try:
    schedule.every().wednesday.at(s.WedK3).do(killzoom)
except:
    pass
try:
    schedule.every().wednesday.at(s.Wed4).do(job)
except:
    pass
try:
    schedule.every().wednesday.at(s.WedK4).do(killzoom)
except:
    pass
try:
    schedule.every().wednesday.at(s.Wed5).do(job)
except:
    pass
try:
    schedule.every().wednesday.at(s.WedK5).do(killzoom)
except:
    pass
try:
    schedule.every().wednesday.at(s.Wed6).do(job)
except:
    pass
try:
    schedule.every().wednesday.at(s.WedK6).do(killzoom)
except:
    pass
try:
    schedule.every().wednesday.at(s.Wed7).do(job)
except:
    pass
try:
    schedule.every().wednesday.at(s.WedK7).do(killzoom)
except:
    pass
# Schedule Thur:
try:
    schedule.every().thursday.at(s.Thu1).do(job)
except:
    pass
try:
    schedule.every().thursday.at(s.ThuK1).do(killzoom)
except:
    pass
try:
    schedule.every().thursday.at(s.Thu2).do(job)
except:
    pass
try:
    schedule.every().thursday.at(s.ThuK2).do(killzoom)
except:
    pass
try:
    schedule.every().thursday.at(s.Thu3).do(job)
except:
    pass
try:
    schedule.every().thursday.at(s.ThuK3).do(killzoom)
except:
    pass
try:
    schedule.every().thursday.at(s.Thu4).do(job)
except:
    pass
try:
    schedule.every().thursday.at(s.ThuK4).do(killzoom)
except:
    pass
try:
    schedule.every().thursday.at(s.Thu5).do(job)
except:
    pass
try:
    schedule.every().thursday.at(s.ThuK5).do(killzoom)
except:
    pass
try:
    schedule.every().thursday.at(s.Thu6).do(job)
except:
    pass
try:
    schedule.every().thursday.at(s.ThuK6).do(killzoom)
except:
    pass
try:
    schedule.every().thursday.at(s.Thu7).do(job)
except:
    pass
try:
    schedule.every().thursday.at(s.ThuK7).do(killzoom)
except:
    pass
# Schedule Fri:
try:
    schedule.every().friday.at(s.Fri1).do(job)
except:
    pass
try:
    schedule.every().friday.at(s.FriK1).do(killzoom)
except:
    pass
try:
    schedule.every().friday.at(s.Fri2).do(job)
except:
    pass
try:
    schedule.every().friday.at(s.FriK2).do(killzoom)
except:
    pass
try:
    schedule.every().friday.at(s.Fri3).do(job)
except:
    pass
try:
    schedule.every().friday.at(s.FriK3).do(killzoom)
except:
    pass
try:
    schedule.every().friday.at(s.Fri4).do(job)
except:
    pass
try:
    schedule.every().friday.at(s.FriK4).do(killzoom)
except:
    pass
try:
    schedule.every().friday.at(s.Fri5).do(job)
except:
    pass
try:
    schedule.every().friday.at(s.FriK5).do(killzoom)
except:
    pass
try:
    schedule.every().friday.at(s.Fri6).do(job)
except:
    pass
try:
    schedule.every().friday.at(s.FriK6).do(killzoom)
except:
    pass
try:
    schedule.every().friday.at(s.Fri7).do(job)
except:
    pass
try:
    schedule.every().friday.at(s.FriK7).do(killzoom)
except:
    pass
# Schedule Sat:
try:
    schedule.every().saturday.at(s.Sat1).do(job)
except:
    pass
try:
    schedule.every().saturday.at(s.SatK1).do(killzoom)
except:
    pass
try:
    schedule.every().saturday.at(s.Sat2).do(job)
except:
    pass
try:
    schedule.every().saturday.at(s.SatK2).do(killzoom)
except:
    pass
try:
    schedule.every().saturday.at(s.Sat3).do(job)
except:
    pass
try:
    schedule.every().saturday.at(s.SatK3).do(killzoom)
except:
    pass
try:
    schedule.every().saturday.at(s.Sat4).do(job)
except:
    pass
try:
    schedule.every().saturday.at(s.SatK4).do(killzoom)
except:
    pass
try:
    schedule.every().saturday.at(s.Sat5).do(job)
except:
    pass
try:
    schedule.every().saturday.at(s.SatK5).do(killzoom)
except:
    pass
try:
    schedule.every().saturday.at(s.Sat6).do(job)
except:
    pass
try:
    schedule.every().saturday.at(s.SatK6).do(killzoom)
except:
    pass
try:
    schedule.every().saturday.at(s.Sat7).do(job)
except:
    pass
try:
    schedule.every().saturday.at(s.SatK7).do(killzoom)
except:
    pass

os.system("cls")
print(f"""{c_blue}
      _               _          ________                              
     / \             / |_       |  __   _|                             
    / _ \    __   _ `| |-' .--. |_/  / /    .--.    .--.   _ .--..--.  
   / ___ \  [  | | | | | / .'`\ \  .'.' _ / .'`\ \/ .'`\ \[ `.-. .-. | 
 _/ /   \ \_ | \_/ |,| |,| \__. |_/ /__/ || \__. || \__. | | | | | | | 
|____| |____|'.__.'_/\__/ '.__.'|________| '.__.'  '.__.' [___||__||__]
                                                                       
{c_yellow}> {c_white}Welcome to {c_blue}AutoZoom{c_white}, a simple tool that joins your zoom meetings automatically.
{c_yellow}> {c_white}Credits to {c_green}Mohammad Alhamoud{c_white}.
{c_yellow}> {c_white}Instructions:
{c_yellow}[1] {c_white}Make sure you've already edited {c_blue}Schedule.xls {c_white}before using the tool.
{c_yellow}[2] {c_blue}AutoZoom {c_white}won't work when you close this window, so keep it open.
""")
while True:
    schedule.run_pending()
    time.sleep(1)
