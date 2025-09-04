import tkinter as tk
import time

root = tk.Tk()
root.title("YOLO")
icon = tk.PhotoImage(file=r"D:\R.png")  
root.iconphoto(True, icon)  # True = 同时设置任务栏图标
root.geometry('450x150+100+10')
root.resizable(0, 0)
root.title('我们的时钟')

# 获取时间的函数
def gettime():
    # 获取当前时间
    dstr.set(time.strftime("%H:%M:%S"))
    # 每隔 1s 调用一次 gettime() 函数来获取时间
    root.after(1000, gettime)

# 生成动态字符串
dstr = tk.StringVar()

# 利用 textvariable 来实现文本变化
lb = tk.Label(root, textvariable=dstr, fg='green', font=("微软雅黑", 85))
lb.pack()

# 调用生成时间的函数
gettime()

# 显示窗口
root.mainloop()
