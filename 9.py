import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import os
import time
import datetime
import json
from pathlib import Path

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("记事本")
        self.root.geometry("800x600")
        
        # 初始化变量
        self.current_file = None
        self.is_saved = True
        self.auto_save_interval = 5  # 自动保存间隔(秒)
        self.recent_files = []
        self.recent_files_max = 10  # 最近文件最大数量
        self.last_save_time = None
        
        # 加载最近文件列表
        self.load_recent_files()
        
        # 创建UI
        self.create_menu()
        self.create_toolbar()
        self.create_text_area()
        self.create_status_bar()
        
        # 设置自动保存
        self.setup_auto_save()
        
        # 绑定事件
        self.bind_events()
    
    def create_menu(self):
        """创建菜单栏"""
        self.menu_bar = tk.Menu(self.root)
        
        # 文件菜单
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        
        # 新建子菜单
        self.new_menu = tk.Menu(self.file_menu, tearoff=0)
        self.new_menu.add_command(label="空白笔记", command=self.new_file)
        self.new_menu.add_separator()
        self.new_menu.add_command(label="待办模板", command=lambda: self.new_from_template("todo"))
        self.new_menu.add_command(label="日记模板", command=lambda: self.new_from_template("diary"))
        self.file_menu.add_cascade(label="新建", menu=self.new_menu)
        
        # 打开菜单
        self.file_menu.add_command(label="打开", command=self.open_file)
        
        # 最近文件子菜单
        self.recent_menu = tk.Menu(self.file_menu, tearoff=0)
        self.update_recent_menu()
        self.file_menu.add_cascade(label="最近打开", menu=self.recent_menu)
        
        self.file_menu.add_separator()
        self.file_menu.add_command(label="保存", command=self.save_file)
        self.file_menu.add_command(label="另存为", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="关闭", command=self.close_file)
        self.file_menu.add_command(label="退出", command=self.quit_app)
        
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)
        
        # 编辑菜单
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="撤销", command=lambda: self.text_area.event_generate("<<Undo>>"))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="剪切", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="复制", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="粘贴", command=lambda: self.text_area.event_generate("<<Paste>>"))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="查找/替换", command=self.find_replace)
        
        self.menu_bar.add_cascade(label="编辑", menu=self.edit_menu)
        
        # 帮助菜单
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="关于", command=self.show_about)
        
        self.menu_bar.add_cascade(label="帮助", menu=self.help_menu)
        
        self.root.config(menu=self.menu_bar)
    
    def create_toolbar(self):
        """创建工具栏"""
        self.toolbar = ttk.Frame(self.root, padding="5")
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # 工具栏按钮
        ttk.Button(self.toolbar, text="新建", command=self.new_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(self.toolbar, text="打开", command=self.open_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(self.toolbar, text="保存", command=self.save_file).pack(side=tk.LEFT, padx=2)
        ttk.Separator(self.toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, padx=5, fill=tk.Y)
        ttk.Button(self.toolbar, text="待办", command=lambda: self.new_from_template("todo")).pack(side=tk.LEFT, padx=2)
        ttk.Button(self.toolbar, text="日记", command=lambda: self.new_from_template("diary")).pack(side=tk.LEFT, padx=2)
    
    def create_text_area(self):
        """创建文本编辑区域"""
        # 创建滚动条
        self.scrollbar = ttk.Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 创建文本区域
        self.text_area = tk.Text(self.root, wrap=tk.WORD, undo=True,
                                yscrollcommand=self.scrollbar.set)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        # 关联滚动条
        self.scrollbar.config(command=self.text_area.yview)
    
    def create_status_bar(self):
        """创建状态栏"""
        self.status_bar = ttk.Label(self.root, text="就绪", anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def bind_events(self):
        """绑定事件处理"""
        self.text_area.bind("<<Modified>>", self.on_text_modified)
        self.root.protocol("WM_DELETE_WINDOW", self.quit_app)
    
    def on_text_modified(self, event):
        """文本修改时更新状态"""
        if self.text_area.edit_modified():
            self.is_saved = False
            self.update_title()
            self.text_area.edit_modified(False)
    
    def update_title(self):
        """更新窗口标题"""
        title = "记事本"
        if self.current_file:
            title += f" - {os.path.basename(self.current_file)}"
        if not self.is_saved:
            title += " (*)"
        self.root.title(title)
    
    def new_file(self):
        """创建新文件"""
        if self.check_unsaved_changes():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.is_saved = True
            self.update_title()
            self.status_bar.config(text="新建空白笔记")
    
    def new_from_template(self, template_type):
        """从模板创建新文件"""
        if self.check_unsaved_changes():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.is_saved = False
            
            if template_type == "todo":
                template = "待办事项列表\n"
                template += "==============\n\n"
                template += "[ ] 任务1\n"
                template += "[ ] 任务2\n"
                template += "[ ] 任务3\n\n"
                template += "备注：\n"
                self.status_bar.config(text="新建待办模板笔记")
            elif template_type == "diary":
                today = datetime.date.today().strftime("%Y年%m月%d日")
                template = f"日记 - {today}\n"
                template += "================\n\n"
                template += "天气：\n\n"
                template += "今日事项：\n\n"
                template += "感想：\n"
                self.status_bar.config(text="新建日记模板笔记")
            
            self.text_area.insert(tk.END, template)
            self.update_title()
    
    def open_file(self):
        """打开文件"""
        if self.check_unsaved_changes():
            file_types = [
                ("所有支持的文件", "*.txt *.md *.markdown *.html"),
                ("文本文件", "*.txt"),
                ("Markdown文件", "*.md *.markdown"),
                ("HTML文件", "*.html"),
                ("所有文件", "*.*")
            ]
            
            file_path = filedialog.askopenfilename(
                defaultextension=".txt",
                filetypes=file_types
            )
            
            if file_path:
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                    
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
                    self.current_file = file_path
                    self.is_saved = True
                    self.add_to_recent_files(file_path)
                    self.update_title()
                    self.status_bar.config(text=f"已打开: {os.path.basename(file_path)}")
                except Exception as e:
                    messagebox.showerror("错误", f"无法打开文件: {str(e)}")
    
    def open_recent_file(self, file_path):
        """打开最近的文件"""
        if os.path.exists(file_path) and self.check_unsaved_changes():
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.current_file = file_path
                self.is_saved = True
                self.add_to_recent_files(file_path)  # 刷新最近文件顺序
                self.update_title()
                self.status_bar.config(text=f"已打开: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("错误", f"无法打开文件: {str(e)}")
                self.remove_from_recent_files(file_path)  # 移除无效文件
        else:
            messagebox.showerror("错误", "文件不存在或已被删除")
            self.remove_from_recent_files(file_path)  # 移除无效文件
    
    def save_file(self):
        """保存文件"""
        if self.current_file:
            try:
                content = self.text_area.get(1.0, tk.END)[:-1]  # 排除最后的换行符
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(content)
                
                self.is_saved = True
                self.last_save_time = time.time()
                self.update_title()
                self.status_bar.config(text=f"已保存: {os.path.basename(self.current_file)}")
                return True
            except Exception as e:
                messagebox.showerror("错误", f"无法保存文件: {str(e)}")
                return False
        else:
            return self.save_as_file()
    
    def save_as_file(self):
        """另存为文件"""
        file_types = [
            ("文本文件", "*.txt"),
            ("Markdown文件", "*.md"),
            ("HTML文件", "*.html"),
            ("所有文件", "*.*")
        ]
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=file_types
        )
        
        if file_path:
            self.current_file = file_path
            result = self.save_file()
            if result:
                self.add_to_recent_files(file_path)
            return result
        return False
    
    def close_file(self):
        """关闭当前文件"""
        if self.check_unsaved_changes():
            self.text_area.delete(1.0, tk.END)
            self.current_file = None
            self.is_saved = True
            self.update_title()
            self.status_bar.config(text="已关闭文件")
    
    def quit_app(self):
        """退出应用程序"""
        if self.check_unsaved_changes():
            self.root.destroy()
    
    def check_unsaved_changes(self):
        """检查是否有未保存的更改"""
        if not self.is_saved:
            response = messagebox.askyesnocancel(
                "未保存的更改",
                "是否保存当前文件的更改？"
            )
            
            if response is None:  # 取消
                return False
            elif response:  # 是
                return self.save_file()
        return True
    
    def setup_auto_save(self):
        """设置自动保存"""
        def auto_save():
            if not self.is_saved and self.current_file:
                try:
                    content = self.text_area.get(1.0, tk.END)[:-1]
                    with open(self.current_file, "w", encoding="utf-8") as file:
                        file.write(content)
                    
                    self.is_saved = True
                    self.last_save_time = time.time()
                    self.update_title()
                    self.status_bar.config(text=f"自动保存: {os.path.basename(self.current_file)}")
                except:
                    pass
            
            # 再次调度自动保存
            self.root.after(self.auto_save_interval * 1000, auto_save)
        
        # 启动自动保存
        self.root.after(self.auto_save_interval * 1000, auto_save)
    
    def find_replace(self):
        """查找替换功能"""
        # 创建查找替换对话框
        dialog = tk.Toplevel(self.root)
        dialog.title("查找和替换")
        dialog.geometry("300x150")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # 查找框
        ttk.Label(dialog, text="查找:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        find_entry = ttk.Entry(dialog, width=25)
        find_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # 替换框
        ttk.Label(dialog, text="替换为:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        replace_entry = ttk.Entry(dialog, width=25)
        replace_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # 按钮
        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        def find_next():
            search_text = find_entry.get()
            if search_text:
                # 从当前位置开始查找
                start_pos = self.text_area.index(tk.INSERT)
                start_pos = self.text_area.index(f"{start_pos}+1c")  # 从下一个字符开始
                
                # 在文本中查找
                pos = self.text_area.search(search_text, start_pos, stopindex=tk.END)
                
                if pos:
                    # 计算结束位置
                    end_pos = f"{pos}+{len(search_text)}c"
                    # 选中找到的文本
                    self.text_area.tag_remove("search", 1.0, tk.END)
                    self.text_area.tag_add("search", pos, end_pos)
                    self.text_area.tag_config("search", background="yellow")
                    self.text_area.mark_set(tk.INSERT, end_pos)
                    self.text_area.see(pos)
                else:
                    messagebox.showinfo("查找", "找不到更多匹配项")
        
        def replace():
            search_text = find_entry.get()
            replace_text = replace_entry.get()
            
            if search_text and self.text_area.tag_ranges("search"):
                # 替换当前选中的文本
                start, end = self.text_area.tag_ranges("search")
                self.text_area.delete(start, end)
                self.text_area.insert(start, replace_text)
                self.text_area.tag_remove("search", 1.0, tk.END)
                # 继续查找下一个
                find_next()
        
        def replace_all():
            search_text = find_entry.get()
            replace_text = replace_entry.get()
            
            if search_text:
                # 从开头开始查找所有匹配项
                self.text_area.tag_remove("search", 1.0, tk.END)
                pos = "1.0"
                count = 0
                
                while True:
                    pos = self.text_area.search(search_text, pos, stopindex=tk.END)
                    if not pos:
                        break
                    
                    end_pos = f"{pos}+{len(search_text)}c"
                    self.text_area.delete(pos, end_pos)
                    self.text_area.insert(pos, replace_text)
                    pos = end_pos
                    count += 1
                
                messagebox.showinfo("替换完成", f"共替换了 {count} 处匹配项")
        
        ttk.Button(button_frame, text="查找下一个", command=find_next).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="替换", command=replace).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="全部替换", command=replace_all).pack(side=tk.LEFT, padx=2)
        
        # 聚焦到查找框
        find_entry.focus_set()
    
    def show_about(self):
        """显示关于对话框"""
        messagebox.showinfo(
            "关于",
            "记事本 v1.0\n\n一个简单但功能齐全的文本编辑器，支持基本的文件操作和文本编辑功能。"
        )
    
    def load_recent_files(self):
        """加载最近文件列表"""
        try:
            config_dir = Path.home() / ".notepad"
            config_dir.mkdir(exist_ok=True)
            config_file = config_dir / "recent_files.json"
            
            if config_file.exists():
                with open(config_file, "r", encoding="utf-8") as f:
                    self.recent_files = json.load(f)
        except:
            self.recent_files = []
    
    def save_recent_files(self):
        """保存最近文件列表"""
        try:
            config_dir = Path.home() / ".notepad"
            config_dir.mkdir(exist_ok=True)
            config_file = config_dir / "recent_files.json"
            
            with open(config_file, "w", encoding="utf-8") as f:
                json.dump(self.recent_files, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存最近文件列表失败: {e}")
    
    def add_to_recent_files(self, file_path):
        """添加文件到最近文件列表"""
        # 如果文件已在列表中，先移除
        if file_path in self.recent_files:
            self.recent_files.remove(file_path)
        
        # 添加到列表开头
        self.recent_files.insert(0, file_path)
        
        # 限制列表长度
        if len(self.recent_files) > self.recent_files_max:
            self.recent_files = self.recent_files[:self.recent_files_max]
        
        # 保存并更新菜单
        self.save_recent_files()
        self.update_recent_menu()
    
    def remove_from_recent_files(self, file_path):
        """从最近文件列表中移除文件"""
        if file_path in self.recent_files:
            self.recent_files.remove(file_path)
            self.save_recent_files()
            self.update_recent_menu()
    
    def update_recent_menu(self):
        """更新最近文件菜单"""
        # 清除现有菜单项
        for item in self.recent_menu.winfo_children():
            self.recent_menu.delete(item)
        
        # 添加最近文件
        if self.recent_files:
            for file_path in self.recent_files:
                # 显示文件名而非完整路径
                display_name = os.path.basename(file_path)
                # 绑定打开文件的命令
                self.recent_menu.add_command(
                    label=display_name,
                    command=lambda path=file_path: self.open_recent_file(path)
                )
            self.recent_menu.add_separator()
            self.recent_menu.add_command(label="清除列表", command=self.clear_recent_files)
        else:
            self.recent_menu.add_command(label="无最近文件", state=tk.DISABLED)
    
    def clear_recent_files(self):
        """清除最近文件列表"""
        self.recent_files = []
        self.save_recent_files()
        self.update_recent_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
