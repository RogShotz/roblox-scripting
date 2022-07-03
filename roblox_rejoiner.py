import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()


# xsrf Generator
def getXsrf():
    authURL = "https://auth.roblox.com/v2/logout"
    xsrfRequest = requests.post(authURL, cookies={
        '.ROBLOSECURITY': os.getenv("ROBLOSEC")
    })
    return xsrfRequest


ticketReq = requests.post("https://auth.roblox.com/v1/authentication-ticket/",
                          headers={"x-csrf-token": getXsrf().headers['x-csrf-token'],
                                   "referer": "https://www.roblox.com/home"},
                          cookies={'.ROBLOSECURITY': os.getenv("ROBLOSEC")})

rbxAuth = ticketReq.headers["rbx-authentication-ticket"]
rbxExecPATH = "C:\\Users\\rogsh\\AppData\\Local\\Roblox\\Versions\\version-cb81695a34b340de\\RobloxPlayerLauncher.exe"
rbxLaunches = "roblox-player:1+launchmode:play+"
rbxGameInfo = f"gameinfo:{rbxAuth}"
rbxLaunchTime = "launchtime:1656807211123"
rbxPlaceLauncherUrl = "placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D129526326804%26placeId%3D9551640993%26isPlayTogetherGame%3Dfalse"
rbxBrowserTrackerId = "browsertrackerid:129526326804"
rbxLocales = "robloxLocale:en_us+gameLocale:en_us+channel:"

while True:
    os.system(
        f'cmd /c "{rbxExecPATH} {rbxLaunches}+{rbxGameInfo}+{rbxLaunchTime}+{rbxPlaceLauncherUrl}+{rbxBrowserTrackerId}+{rbxLocales}"')
    print("Starting New Session")
    time.sleep(1800)
