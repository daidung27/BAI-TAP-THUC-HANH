from tkinter import *
from tkinter import messagebox

def NewFile():
    """Hiển thị thông báo khi chọn 'New'."""
    messagebox.showinfo("Lệnh Menu", "Bạn đã chọn tạo Tệp mới (New File!)") 

def OpenFile():
    """Hiển thị thông báo khi chọn 'Open'."""
    messagebox.showinfo("Lệnh Menu", "Bạn đã chọn Mở Tệp (Open File!)")

def InsText():
    """Hiển thị thông báo khi chọn 'Insert -> Text'."""
    messagebox.showinfo("Lệnh Menu", "Bạn đã chọn Chèn Văn bản (Insert Text!)") 

def InsPic():
    """Hiển thị thông báo khi chọn 'Insert -> Picture'."""
    messagebox.showinfo("Lệnh Menu", "Bạn đã chọn Chèn Ảnh (Insert Picture!)") 

def About():
    """Hiển thị thông báo khi chọn 'Help -> About...'."""
    messagebox.showinfo("Giới thiệu", "Đây là ứng dụng ví dụ về Menu sử dụng Tkinter.")

root = Tk()
root.title("tk") 
menu = Menu(root)
root.config(menu=menu) 
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile) 
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=root.quit) 
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)

insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu) 

helpmenu.add_command(label="About...", command=About)

root.mainloop()
