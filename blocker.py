import psutil, os, json, time, platform
CONFIG_PATH = "config/blocked_apps.json"
def load_block_list():
    with open(CONFIG_PATH) as f: data = json.load(f)
    return data["blocked_apps"], data["blocked_websites"]
def block_apps(duration):
    blocked_apps,_=load_block_list(); end=time.time()+duration*60
    while time.time()<end:
        for p in psutil.process_iter(['name']):
            try:
                if p.info['name'] in blocked_apps: p.kill()
            except: pass
        time.sleep(3)
def block_websites(duration):
    _,sites=load_block_list()
    hosts=r"C:\Windows\System32\drivers\etc\hosts" if platform.system()=="Windows" else "/etc/hosts"
    redir="127.0.0.1"; end=time.time()+duration*60
    with open(hosts,"a") as f:
        for s in sites: f.write(f"{redir} {s}\n")
    try:
        while time.time()<end: time.sleep(10)
    finally:
        lines=open(hosts).readlines()
        open(hosts,"w").writelines(l for l in lines if not any(s in l for s in sites))
