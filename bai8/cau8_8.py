print('họ tên: TONG DOAN DAI DUNG; MSV:245752021610009')
import tkinter as tk
from tkinter import messagebox

# ==================== FORM A: THÔNG TIN CÁ NHÂN ====================
def create_personal_info_form():
    info_window = tk.Toplevel()
    info_window.title("Thông tin cá nhân")
    info_window.geometry("350x180")
    
    def show_info():
        ho_ten = entry_name.get()
        mssv = entry_id.get()
        messagebox.showinfo(
            "Thông tin đã nhập",
            f"Họ tên: {ho_ten}\nMSSV: {mssv}"
        )
        
    label_name = tk.Label(info_window, text="Họ tên:")
    label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    entry_name = tk.Entry(info_window, width=30)
    entry_name.grid(row=0, column=1, padx=10, pady=10)
    entry_name.insert(0, "TONG DOAN DAI DUNG")
    

    label_id = tk.Label(info_window, text="MSSV:")
    label_id.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    
    entry_id = tk.Entry(info_window, width=30)
    entry_id.grid(row=1, column=1, padx=10, pady=10)
    
    entry_id.insert(0, "245752021610009")
    
    
    button_show = tk.Button(
        info_window,
        text="Hiển thị thông tin",
        command=show_info  
    )

    button_show.grid(row=2, column=0, columnspan=2, pady=10)

    info_window.grab_set() 
    info_window.focus_set()
    info_window.wait_window()

# ==================== CHẠY CHƯƠNG TRÌNH ====================

root = tk.Tk()
root.withdraw()

create_personal_info_form()

root.mainloop()
