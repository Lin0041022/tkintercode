import tkinter as tk
win = tk.Tk()
win.title("C语言中文网")
win.geometry('400x200')
icon = tk.PhotoImage(file=r"D:\R.png")  
win.iconphoto(True, icon)  # True = 同时设置任务栏图标
# 若内容是文字则以字符为单位，图像则以像素为单位
label = tk.Label(win, text="网址：c.biancheng.net",font=('宋体',20, 'bold italic'),bg="#7CCD7C",
                 # 设置标签内容区大小
                 width=30,height=5,
                 # 设置填充区距离、边框宽度和其样式（凹陷式）
                 padx=10, pady=15, borderwidth=10, relief="sunken")
label.pack()
win.mainloop()