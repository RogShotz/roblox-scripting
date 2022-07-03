import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()


def kill_by_process_name_shell(name):
    os.system("taskkill /f /im " + name)


# xsrf Generator
def getXsrf():
    authURL = "https://auth.roblox.com/v2/logout"
    xsrfRequest = requests.post(authURL, cookies={
        '.ROBLOSECURITY': os.getenv("ROBLOSEC")
    })
    return xsrfRequest


def getAutTicket():
    ticketReq = requests.post("https://auth.roblox.com/v1/authentication-ticket/",
                              headers={"x-csrf-token": getXsrf().headers['x-csrf-token'],
                                       "referer": "https://www.roblox.com/home"},
                              cookies={'.ROBLOSECURITY': os.getenv("ROBLOSEC")})
    return ticketReq.headers["rbx-authentication-ticket"]


# Computer\HKEY_CLASSES_ROOT\roblox-player\shell\open\command
rbxExecPATH = "C:\\Users\\rogsh\\Downloads\\synapse-launcher-11-17-21\\bin\\9QqpqI5vxy28.exe"
rbxLaunches = "roblox-player:1+launchmode:play+"
rbxGameInfo = f"gameinfo:{getAutTicket()}"
rbxLaunchTime = "launchtime:1656807211123"
rbxPlaceLauncherUrl = "placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D129526326804%26placeId%3D9551640993%26isPlayTogetherGame%3Dfalse"
rbxBrowserTrackerId = "browsertrackerid:129526326804"
rbxLocales = "robloxLocale:en_us+gameLocale:en_us+channel:"


os.system(
        f'cmd /c "C:\\Users\\rogsh\\Downloads\\synapse-launcher-11-17-21\\Synapse Launcher.exe"')
time.sleep(7)
while True:
    os.system(
       f'cmd /c "{rbxExecPATH} {rbxLaunches}+{rbxGameInfo}+{rbxLaunchTime}+{rbxPlaceLauncherUrl}+{rbxBrowserTrackerId}+{rbxLocales}"')
    print("Starting New Session")
    time.sleep(20)
    kill_by_process_name_shell("RobloxPlayerBeta.exe")
    time.sleep(1)
    rbxGameInfo = f"gameinfo:{getAutTicket()}"
    time.sleep(5)
