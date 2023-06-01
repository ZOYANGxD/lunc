import requests,json
from colorama import Fore
config = json.load(open('config.json'))

def payload(service:str="capsolver.com", proxy:str=None, user_agent:str=None) -> None:
    p = {
        "clientKey":config["capsolver"],
        "task": {
            "websiteURL":"https://discord.com/",
            "websiteKey":"4c672d35-0701-42b2-88c3-78380b0db560",
        }
    }
    if service == "capsolver.com": 
        p['appId']="942A346E-6C5A-4AE8-B2DE-24E6F9444EA4"
        p['task']['type'] = "HCaptchaTurboTask"
        p['task']['proxy'] = proxy 
        p['task']['userAgent'] = user_agent
    if service == "capmonster.cloud": 
        p['task']['type'] = "HCaptchaTask"
        p['task']['proxyType'] = "http"
        p['task']['proxyAddress'] = proxy.split("@")[1].split(":")[0]
        p['task']['proxyPort'] = proxy.split("@")[1].split(":")[1]
        p['task']['proxyLogin'] = proxy.split("@")[0].split(":")[0]
        p['task']['proxyPassword'] = proxy.split("@")[0].split(":")[1]
    return p

def solve_captcha(proxy,ua):
    # Creating a task
    # proxy = proxy.replace("http://","").replace("/","")
    # proxy = f"http://{proxy}"
    r = requests.post(f"https://api.capsolver.com/createTask",json=payload("capsolver.com",proxy,ua))
    try:
        if r.json().get("taskId"):
            taskid = r.json()["taskId"]
            print(f"({Fore.YELLOW}~{Fore.WHITE}) SOLVING CAPTCHA {taskid}....", flush=True)
        else:
            print("Couldn't retrieve captcha task id.",r.text,"failed")
            return "failed"
    except:
        print("Couldn't retrieve captcha task id.",r.text,"failed")
        return "failed"
    # Waiting for results
    while True:
        try:
            r = requests.post(f"https://api.capsolver.com/getTaskResult",json={"clientKey":config["capsolver"],"taskId":taskid})
            if r.json()["status"] == "ready":
                key = r.json()["solution"]["gRecaptchaResponse"]
                print(f"({Fore.YELLOW}~{Fore.WHITE}) Captcha Solved ({Fore.RED}{key[:40]}..{Fore.WHITE})", flush=True)
                return key
            elif r.json()['status'] == "failed":
                return "failed"
        except:
            print("Failed to get solving status.",r.text,"failed")
            return "failed"
