print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
import tkinter as tk
root = tk.Tk()
root.title("Choose your favourite programming language")
v = tk.IntVar()
v.set(1) 
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C#", 5)
]
def ShowChoice():
    print(f"Selected language value: {v.get()}")
    for lang, val in languages:
        if val == v.get():
            print(f"Selected language name: {lang}")
            break
tk.Label(
    root,
    text="""Choose your favourite
programming language:""",
    justify=tk.LEFT,
    padx=20 
).pack(anchor=tk.W) 
for language, val in languages:
    tk.Radiobutton(
        root,
        text=language,       
        padx=20,             
        variable=v,          
        value=val,          
        command=ShowChoice   
    ).pack(anchor=tk.W)       

root.mainloop()
