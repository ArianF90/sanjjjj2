import tkinter as tk
from tkinter import ttk
import time
import random

def start_check():
    progress['value'] = 0
    status['text'] = "در حال سنجش..."
    for i in range(100):
        progress['value'] += 1
        window.update_idletasks()
        time.sleep(0.1)
    status['text'] = ""
    user_name = entry.get()
    result['text'] = f'{user_name} عزیزززز :)، درصد گی بودن شما: {random.randint(0, 100)}%'

def show_message():
    message_label.pack(pady=10)
    window.update()
    time.sleep(5)
    message_label.pack_forget()
    start_interface()

def start_interface():
    label.pack(pady=10)
    entry_label.pack(pady=5)
    entry.pack(pady=5)
    button.pack(pady=10)
    progress.pack(pady=10)
    status.pack(pady=5)
    result.pack(pady=10)

window = tk.Tk()
window.title("گی سنج")
window.geometry("400x300")
window.config(bg="#f0f8ff")

message_label = tk.Label(window, text="کاری از عمو آرین", font=('Fedra Arabic', 18, 'bold'), bg="#f0f8ff", fg="#483d8b")

label = tk.Label(window, text="گی سنج", font=('Fedra Arabic', 18, 'bold'), bg="#f0f8ff", fg="#483d8b")
entry_label = tk.Label(window, text="نام خود را وارد کنید:", font=('Fedra Arabic', 14), bg="#f0f8ff", fg="#483d8b")
entry = tk.Entry(window, font=('Fedra Arabic', 14))
button = tk.Button(window, text="سنجیدن", command=start_check, font=('Fedra Arabic', 14), bg="#87ceeb", fg="#ffffff")
progress = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=300, mode='determinate')
status = tk.Label(window, text="", font=('Fedra Arabic', 12), bg="#f0f8ff", fg="#483d8b")
result = tk.Label(window, font=('Fedra Arabic', 14), bg="#f0f8ff", fg="#483d8b")

show_message()
window.mainloop()
