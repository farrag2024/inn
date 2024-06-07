import tkinter as tk
from tkinter import messagebox
import webbrowser

def open_link1():
    webbrowser.open("https://farrag2024.github.io/inter.d/")

def open_link2():
    password = password_entry.get()
    if password == "1234":
        webbrowser.open("https://www.example2.com")
    else:
        messagebox.showerror("خطأ", "كلمة المرور غير صحيحة")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("تطبيق الروابط")

# ضبط حجم النافذة
root.geometry("300x200")

# زر لفتح الرابط الأول
link1_button = tk.Button(root, text="افتح الرابط الأول", command=open_link1)
link1_button.pack(pady=10)

# إدخال كلمة المرور وزر لفتح الرابط الثاني
password_label = tk.Label(root, text="أدخل كلمة المرور:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

link2_button = tk.Button(root, text="افتح الرابط الثاني", command=open_link2)
link2_button.pack(pady=10)

# زر الخروج من التطبيق
exit_button = tk.Button(root, text="خروج", command=exit_app)
exit_button.pack(pady=10)

root.mainloop()
