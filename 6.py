# import tkinter as tk
# from tkinter import messagebox

# win = tk.Tk()
# # 设置主窗口
# win.geometry('250x200+250+200')
# win.title("C语言中文网")
# icon = tk.PhotoImage(file=r"D:\R.png")  
# win.iconphoto(True, icon)  # True = 同时设置任务栏图标
# win.resizable(0,0)

# # 创建验证函数
# def check():
#     if entry1.get() == "C语言中文网":
#         messagebox.showinfo("输入正确")
#         return True
#     else:
#         messagebox.showwarning("输入不正确")
#         entry1.delete(0,tk.END)
#         return False
# def check1():
#     if entry2.get() == "123":
#         messagebox.showinfo("输入正确")
#         return True
#     else:
#         messagebox.showwarning("输入不正确")
#         entry2.delete(0,tk.END)
#         return False
# # 新建文本标签
# labe1 = tk.Label(win,text="账号：")
# labe2 = tk.Label(win,text="密码：")
# labe1.grid(row=0)
# labe2.grid(row=1)
# # 创建动字符串
# Dy_String = tk.StringVar()
# # 使用验证参数 validata,参数值为 focusout 当失去焦点的时候，验证输入框内容是否正确
# entry1 = tk.Entry(win,textvariable =Dy_String,validate ="focusout",validatecommand=check)
# entry2 = tk.Entry(win,textvariable =Dy_String,validate ="focusout",validatecommand=check1)

# # 对控件进行布局管理，放在文本标签的后面
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)

# win.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# win = tk.Tk()
# win.geometry('250x200+250+200')
# win.title("登录窗口")
# icon = tk.PhotoImage(file=r"D:\R.png")  
# win.iconphoto(True, icon)  
# win.resizable(0, 0)

# # 创建登录验证函数
# def login_check():
#     username = entry1.get().strip()
#     password = entry2.get().strip()

#     correct_user = "C语言中文网"#账号为数字
#     correct_pass = "123"#密码包含大小写和特殊符号

#     if username == "" or password == "":
#         messagebox.showwarning("警告", "账号或密码不能为空！")
#     elif username == correct_user and password == correct_pass:
#         messagebox.showinfo("成功", "登录成功！")
#         win.destroy()  # 登录成功后关闭窗口（可根据需求改成跳转主界面）
#     else:
#         messagebox.showerror("错误", "账号或密码错误，请重新输入！")
#         entry2.delete(0, tk.END)  # 只清空密码，避免用户每次都重新输账号

# # 新建文本标签
# label1 = tk.Label(win, text="账号：")
# label2 = tk.Label(win, text="密码：")
# label1.grid(row=0, column=0, padx=10, pady=10)
# label2.grid(row=1, column=0, padx=10, pady=10)

# # 创建输入框
# entry1 = tk.Entry(win)
# entry2 = tk.Entry(win, show="*")  # 密码输入时显示为 *

# entry1.grid(row=0, column=1, padx=10, pady=10)
# entry2.grid(row=1, column=1, padx=10, pady=10)

# # 登录按钮
# btn_login = tk.Button(win, text="登录", command=login_check)
# btn_login.grid(row=2, columnspan=2, pady=20)

# win.mainloop()

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry('300x220+250+200')
win.title("登录窗口")
icon = tk.PhotoImage(file=r"D:\R.png")  
win.iconphoto(True, icon)  
win.resizable(0, 0)

# 登录验证函数
def login_check():
    username = entry1.get().strip()
    password = entry2.get().strip()

    # 模拟数据库里的账号密码
    correct_user = "123456"
    correct_pass = "Aa@123"

    # 账号必须是数字
    if not username.isdigit():
        messagebox.showwarning("警告", "账号必须是纯数字！")
        return

    # 密码必须包含大写字母、小写字母和特殊符号
    special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_nanum = any(c.isdigit() for c in password)
    has_special = any(c in special_chars for c in password)

    if not (has_upper and has_lower):
        messagebox.showwarning("警告", "密码必须包含大小写字母！")
        return
    if not(has_nanum):
        messagebox.showwarning("警告", "密码必须包含数字！")
        return
    if not(has_special):
        messagebox.showwarning("警告", "密码必须包含特殊符号！")
        return
    
    # 验证账号密码是否正确
    if username == correct_user and password == correct_pass:
        messagebox.showinfo("成功", "登录成功！")
        win.destroy()
    else:
        messagebox.showerror("错误", "账号或密码错误，请重新输入！")
        entry2.delete(0, tk.END)  # 只清空密码

# 新建文本标签
label1 = tk.Label(win, text="账号：")
label2 = tk.Label(win, text="密码：")
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)

# 输入框
entry1 = tk.Entry(win)
entry2 = tk.Entry(win, show="*")

entry1.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

# 登录按钮
btn_login = tk.Button(win, text="登录", command=login_check)
btn_login.grid(row=2, columnspan=2, pady=20)

win.mainloop()
