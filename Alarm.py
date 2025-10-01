import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
from playsound import playsound  # pip install playsound

def set_alarm():
    alarm_time = f"{hour_var.get()}:{minute_var.get()}:{second_var.get()}"
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    threading.Thread(target=alarm_thread, args=(alarm_time,)).start()

def alarm_thread(alarm_time):
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            playsound("alarm.mp3")  # aap apni alarm.mp3 file path yahan dalen
            messagebox.showinfo("Alarm", "Wake Up! ⏰")
            break
        time.sleep(1)

# GUI setup
root = tk.Tk()
root.title("Alarm Clock")

tk.Label(root, text="Set Alarm (HH:MM:SS)").pack()

hour_var = tk.StringVar()
minute_var = tk.StringVar()
second_var = tk.StringVar()

tk.Entry(root, textvariable=hour_var, width=3).pack(side="left")
tk.Label(root, text=":").pack(side="left")
tk.Entry(root, textvariable=minute_var, width=3).pack(side="left")
tk.Label(root, text=":").pack(side="left")
tk.Entry(root, textvariable=second_var, width=3).pack(side="left")

tk.Button(root, text="Set Alarm", command=set_alarm).pack()

root.mainloop()

