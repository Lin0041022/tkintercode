# # import tkinter as tk
# # root= tk.Tk()
# # root.title("yolo")
# # root.geometry("500x500+300+300")
# # icon = tk.PhotoImage(file=r"D:\R.png")  
# # root.iconphoto(True, icon)  # True = 同时设置任务栏图标
# # w=tk.Spinbox(root,from_=0,to=20,increment=2,width=15,bg='#9BCD98')
# # w.pack()
# # root.mainloop()



# # import tkinter as tk
# # root= tk.Tk()
# # root.title("C语言中文网")
# # root.geometry("300x200+300+300")
# # icon = tk.PhotoImage(file=r"D:\R.png")  
# # root.iconphoto(True, icon)
# # string=tk.Spinbox(root,values=('Python','C语言','C++','Java','PHP'))
# # string.pack()
# # root.mainloop()


# # from tkinter import *

# # win = Tk()
# # win.title("C语言中文网")
# # icon = PhotoImage(file=r"D:\R.png")  
# # win.iconphoto(True, icon)
# # win.geometry('400x420')
# # text = Text(win, width=50, height=30, undo=True, autoseparators=False)
# # text.pack()
# # text.insert(INSERT, 'C语言中文网，一个有温度的网站')
# # win.mainloop()


# # from tkinter import *
# # win = Tk()
# # win.title("YOLO")
# # win.geometry('400x420')
# # text=Text(win,width=50,height=30,undo=True,autoseparators=False)
# # text.grid()
# # text.insert(INSERT,'YOLO,一个有温度的网站')
# # def backout():
# #     text.edit_undo()
# # def regain():
# #     text.edit_redo()
# # Button(win,text='返回',command=backout).grid(row=3,column=0,sticky="w",padx=10,pady=5)
# # Button(win,text='恢复',command=regain).grid(row=3,column=1,sticky="e",padx=10,pady=5)
# # win.mainloop()

# # from tkinter import *
# # import tkinter.messagebox
# # win=Tk()
# # win.config(bg='#9BCD98')
# # win.title("YOLO")
# # win.geometry('400x420')

# # def menuCommand():
# #     tkinter.messagebox.showinfo('主菜单栏','你正在使用主菜单栏')
# # main_menu=Menu(win)
# # main_menu.add_command(label='文件',command=menuCommand)
# # main_menu.add_command(label='编辑',command=menuCommand)
# # main_menu.add_command(label='格式',command=menuCommand)
# # main_menu.add_command(label='查看',command=menuCommand)
# # main_menu.add_command(label='帮助',command=menuCommand)

# # win.config(menu=main_menu)
# # win.mainloop()


# # import tkinter as tk

# # root=tk.Tk()
# # root.configure(bg='#9BCD98')
# # root.title("YOLO")
# # root.geometry('400x420')
# # def func():
# #     print('您通过弹出菜单执行了命令')

# # menu = tk.Menu(root,tearoff=False)
# # menu.add_command(label='新建',command=func)
# # menu.add_command(label='复制',command=func)
# # menu.add_command(label='粘贴',command=func)
# # menu.add_command(label='剪切',command=func)

# # def command(event):
# #     menu.post(event.x_root,event.y_root)

# # root.bind('<Button-3>',command)
# # root.mainloop()

# from tkinter import *
# import tkinter.messagebox
# win=Tk()
# win.configure(bg='#9BCD98')
# win.title("YOLO")
# win.geometry('400x420+300+300')
# def menuCommand():
#     tkinter.messagebox.showinfo('下拉菜单','你正在使用主菜单栏')
# main_menu = Menu(win)
# filemenu = Menu(main_menu,tearoff=False)
# filemenu.add_command(label='新建',command=menuCommand,accelerator='Ctrl+N')
# filemenu.add_command(label='打开',command=menuCommand,accelerator='Ctrl+O')
# filemenu.add_command(label='保存',command=menuCommand,accelerator='Ctrl+S')
# filemenu.add_separator()
# filemenu.add_command(label='退出',command=win.quit)
# main_menu.add_cascade(label='文件',menu=filemenu)
# win.config(menu=main_menu)
# win.bind("<Control-n>",menuCommand)
# win.bind("<Control-N>",menuCommand)
# win.bind("<Control-o>",menuCommand)
# win.bind("<Control-O>",menuCommand)
# win.bind("<Control-s>",menuCommand)
# win.bind("<Control-S>",menuCommand)
# win.mainloop()


# import tkinter as tk
# win=tk.Tk()
# win.title("YOLO")
# win.geometry('400x420+300+300')
# frame1=tk.Frame(win)
# frame1.pack()
# frame_left=tk.Frame(frame1)
# tk.Label(frame_left,text='左侧标签1',bg='green',width=10,height=5).grid(row=0,column=0)
# tk.Label(frame_left,text='左侧标签2',bg='yellow',width=10,height=5).grid(row=1,column=1)
# frame_left.pack(side=tk.LEFT)

# frame_right=tk.Frame(frame1)
# tk.Label(frame_right,text='右侧标签1',bg='green',width=10,height=5).grid(row=0,column=1)
# tk.Label(frame_right,text='右侧标签2',bg='yellow',width=10,height=5).grid(row=1,column=0)
# tk.Label(frame_right,text='右侧标签2',bg='pink',width=10,height=5).grid(row=1,column=1)
# frame_right.pack(side=tk.RIGHT)
# win.mainloop()

from tkinter import *
win=Tk()
win.title("YOLO")
win.geometry('400x420+300+300')
win.configure(bg='#9BCD98')

for i in range(36):
    for j in range(36):
        Button (win,text=f'{i},{j}',bg='#9BCD98').grid(row=i,column=j)

Label(win,text='YOLO',bg='#9BCD98').grid(row=5,column=8)
win.mainloop()