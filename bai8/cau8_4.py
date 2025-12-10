print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
import tkinter as tk
from tkinter import messagebox
class UngDungGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ứng dụng Tkinter OOP")
        master.geometry("350x150")
        self.nut_chuc_nang = tk.Button(
            master,
            text="Nhấn tôi!",
            fg="white",  
            bg="blue",   
            font=('Arial', 12, 'bold'), 
            command=self.xu_ly_su_kien 
        )
        self.nut_chuc_nang.grid(row=0, column=0, padx=100, pady=50)

    def xu_ly_su_kien(self):
        """
        Phương thức được gọi khi nut_chuc_nang được nhấn.
        """
        thong_bao = "Chào mừng đến với lập trình hướng đối tượng GUI!"
        print(f"Sự kiện nút bấm: {thong_bao}")
        messagebox.showwarning("Cảnh báo Nhấn nút", thong_bao)

if __name__ == '__main__':
    cua_so_goc = tk.Tk()
    ung_dung = UngDungGUI(cua_so_goc)
    cua_so_goc.mainloop()
