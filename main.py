import threading, tkinter as tk
from tkinter import messagebox
from blocker import block_apps, block_websites
from startup_manager import add_to_startup, remove_from_startup
def start():
    try:
        d=int(e.get())
        if d<=0: raise ValueError
        messagebox.showinfo("FocusGuard",f"Running for {d} minutes")
        threading.Thread(target=block_apps,args=(d,),daemon=True).start()
        threading.Thread(target=block_websites,args=(d,),daemon=True).start()
    except: messagebox.showerror("Error","Enter valid duration")
root=tk.Tk(); root.title("FocusGuard"); root.geometry("400x300"); root.config(bg='#1E1E1E')
tk.Label(root,text='🧠 FocusGuard',font=('Arial',18,'bold'),fg='#00FF88',bg='#1E1E1E').pack(pady=10)
tk.Label(root,text='Enter Focus Duration (minutes):',font=('Arial',12),bg='#1E1E1E',fg='white').pack()
e=tk.Entry(root,width=10,font=('Arial',12)); e.pack(pady=5)
tk.Button(root,text='Start Focus Mode',command=start,bg='#00FF88',font=('Arial',12,'bold')).pack(pady=10)
tk.Button(root,text='Enable Auto Start',command=lambda:[add_to_startup(),messagebox.showinfo("Info","Enabled")],
          bg='#007BFF',fg='white').pack(pady=3)
tk.Button(root,text='Disable Auto Start',command=lambda:[remove_from_startup(),messagebox.showinfo("Info","Disabled")],
          bg='#FF4444',fg='white').pack(pady=3)
root.mainloop()
