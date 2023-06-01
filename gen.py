__author__ = '𝐂𝐘 〢! ~ GoKu xD#0639 & Cuckoo#0001'

import requests
from colorama import Fore
import colorama, os, sys
colorama.init(convert=True)
from tls_client import Session
import threading; from threading import Lock, Thread
import time, random, colorama, json, ctypes, names
from solver import solve_captcha; from pystyle import Write, Colors, Center
from concurrent.futures import ThreadPoolExecutor; import hashlib
from licensing.methods import Key, Helpers; import email
from licensing.models import *; import string, imaplib
from websocket import WebSocket

colorama.init(convert=True)

unlocked = 0; locked = 1; captchas = 0; count = 0; gen_start = time.time()


ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
xtrack = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
os.system("cls") if os.name == "nt" else os.system("clear")
ctypes.windll.kernel32.SetConsoleTitleW(f'Senpai gen 3.0 | unlocked rate: {round(count/(count+locked)*100)}% | generated: {count} | unlocked {unlocked} | locked 0')

class Generator:
    def __init__(self, headers=None) -> None:
        self.headers = headers
        self.tls_session = Session(
            client_identifier="chrome_113",
            pseudo_header_order=[":authority",":method",":path",":scheme"],
            header_order=["accept","accept-encoding","accept-language","user-agent"],
            random_tls_extension_order=True
        )

        self.proxies = random.choice(open('proxies.txt', 'r').read().splitlines())
        self.proxy = {
            "http": "http://"+self.proxies,
            "https": "http://"+self.proxies
        }
        self.client_build = 198318

    def cprint(self, use_case, content):
        # lock = threading.Lock()
        if use_case == 'SUCCESS':
            print(f"({Fore.GREEN}${Fore.WHITE}) {content}", flush=True)
        if use_case == 'INFO':
            print(f"({Fore.BLUE}~{Fore.WHITE}) {content}", flush=True)
        if use_case == 'ERROR':
            print(f"({Fore.RED}-{Fore.WHITE}) {content}", flush=True)
        if use_case == 'WARN':
            print(f"({Fore.YELLOW}!{Fore.WHITE}) {content}", flush=True)
        # lock.acquire()
        # lock.release()

    def reg_disc(self, invite) -> None:
        global count
        global unlocked
        global locked
        session = self.tls_session

        # extract cookie dict

        fing_headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://discord.com/',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'x-track': xtrack,
        }
        nameeee = random.choice(open('usernames.txt', 'r', encoding="utf-8").read().splitlines())

        try:
            cookie = requests.get("https://discord.com/app", headers=fing_headers).cookies.get_dict()
        except:
            self.cprint("ERROR", "Cookie cant be extracted from request http://discord.com/app.")

        capKey = solve_captcha("http://"+self.proxies,ua)
        if invite == "" or None:
            payload = {
                "fingerprint": requests.get("https://discord.com/api/v9/experiments", headers=fing_headers).json()["fingerprint"],
                "consent": True,
                "username": nameeee,
                "captcha_key": capKey,
            }
        else:
            payload = {
                "fingerprint": requests.get("https://discord.com/api/v9/experiments", headers=fing_headers).json()["fingerprint"],
                "consent": True,
                "username": nameeee,
                "captcha_key": capKey,
                "invite": invite
            }
            # print()
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'Connection': 'keep-alive',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'x-fingerprint': requests.get("https://discord.com/api/v9/experiments", headers=fing_headers).json()["fingerprint"],
            'x-track': xtrack,
        }
        try:
            try:
                response = session.post('https://discord.com/api/v9/auth/register', headers=headers, cookies=cookie, json=payload)
                if 'token' not in response.text:
                    self.cprint("ERROR", "Can't generate token. %s"%response.text)
                    return "failed"
            except Exception as e:
                return self.cprint("WARN", "EXCEPTION %s"%e)
        except requests.exceptions.ProxyError as er:
            return self.cprint("ERROR", f"Proxy Error {er}")
        
        token = response.json().get('token')

        checker = requests.get("https://discord.com/api/v10/users/@me/library", headers={"Authorization": token})

        if checker.status_code != 200:
            self.cprint("WARN", f"Token Locked {token}")
            locked+=1
            return "locked token"
        
        self.cprint("SUCCESS", "Token Generated {}".format(token))

        unlocked+=1
        count+=1
        ctypes.windll.kernel32.SetConsoleTitleW(f'Senpai gen 3.0 | unlocked rate: {round(count/(count+locked)*100)}% | generated: {count} | unlocked {unlocked} | locked {locked} | generator speed: {round(count / ((time.time() - gen_start) / 60))}/m')

        with open("tokens.txt", "a") as f:
            f.write(f"{token}\n")

    def __thread__(self, threads, invite):
        self.tls_session.proxies = "http://"+self.proxies
        if threading.active_count() < int(threads):
            threading.Thread(target=self.reg_disc, args=(invite,)).start()

if __name__ == "__main__":
    ### MAIN ###
    logo = """
    ██████ ▓█████  ███▄    █  ██▓███   ▄▄▄       ██▓
    ▒██    ▒ ▓█   ▀  ██ ▀█   █ ▓██░  ██▒▒████▄    ▓██▒
    ░ ▓██▄   ▒███   ▓██  ▀█ ██▒▓██░ ██▓▒▒██  ▀█▄  ▒██▒
    ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ░██░
    ▒██████▒▒░▒████▒▒██░   ▓██░▒██▒ ░  ░ ▓█   ▓██▒░██░
    ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░░▓  
    ░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░░▒ ░       ▒   ▒▒ ░ ▒ ░
    ░  ░  ░     ░      ░   ░ ░ ░░         ░   ▒    ▒ ░
        ░     ░  ░         ░                ░  ░ ░  

    """
    Write.Print(Center.XCenter(logo), Colors.blue_to_purple, interval=0.000)

    max_threads = int(Write.Input("\n   Threads -> ", Colors.red_to_black, interval=0.0025))
    # tokens_name = Write.Input("\n   Tokens username (0 for random) -> ", Colors.red_to_black, interval=0.0025)
    invite = Write.Input("\n   Invite (leave blank to not make them join) -> ", Colors.red_to_black, interval=0.0025)
    # license_keyyyy = Write.Input("\n   License key -> ", Colors.red_to_black, interval=0.0025)
    # RSAPubKey = "<RSAKeyValue><Modulus>t5Xlelp74pqU2sHwB/q2J7y+p75paukH797Ef/kma3+E37eJNEq6nIP0/5vWaRZtB1XV25c4dm6thzn0Is8LSdgvZDt98fyZRsCS2uZA0PN6UlO9oqHugYIZZ1cG9tzlwwsDJkGDmE0KJQHkxO/ECM+d/ZVMtLnBQ4+B6sCzQZL76yewkq6P4lIncyEPhOJO7ONso5eT85KRF9/bzOz51EukDyRocOhAzr108FVf0aGfuDnSZ1r71TRYK+WlnExaXEVCgOb1lrr0eCsS+rgfZbT/qMO5e6HuQDaW0FoGidKqiTFzj+3cd7bjqh7DYuYIlg/NC/vJvAhOWSJmbeZbkQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
    # auth = "WyI0OTA2NTUyMCIsIjA5UFhOMjJnYk5pdWgvN2svczR6M3Y3Uk5WV0FFR1hwTTRhZHhBMkIiXQ=="

    # result = Key.activate(token=auth,\
    #                 rsa_pub_key=RSAPubKey,\
    #                 product_id=20214, \
    #                 key=license_keyyyy,\
    #                 machine_code=Helpers.GetMachineCode(v=2))

    # if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
    #     print("The license does not work: {0}".format(result[1]))
    #     time.sleep(60)
    #     sys.exit()
    # else:
    #     pass

    print("\n")
    try:
        while True:
            Generator().__thread__(max_threads+1, invite)
    except KeyboardInterrupt:
        sys.exit()