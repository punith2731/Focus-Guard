import os, platform
APP="FocusGuard"; PATH=os.path.abspath("main.py")
def add_to_startup():
    if platform.system()=="Windows":
        sf=os.path.join(os.getenv('APPDATA'),"Microsoft\Windows\Start Menu\Programs\Startup")
        open(os.path.join(sf,f"{APP}.bat"),"w").write(f'start "" python "{PATH}"\n')
    elif platform.system()=="Linux":
        d=os.path.expanduser("~/.config/autostart/"); os.makedirs(d,exist_ok=True)
        f=os.path.join(d,f"{APP}.desktop")
        open(f,"w").write(f"[Desktop Entry]\nType=Application\nExec=python3 {PATH}\nName={APP}\n")
def remove_from_startup():
    if platform.system()=="Windows":
        sf=os.path.join(os.getenv('APPDATA'),"Microsoft\Windows\Start Menu\Programs\Startup")
        f=os.path.join(sf,f"{APP}.bat"); os.remove(f) if os.path.exists(f) else None
    elif platform.system()=="Linux":
        f=os.path.expanduser(f"~/.config/autostart/{APP}.desktop"); os.remove(f) if os.path.exists(f) else None
