print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
S= input('Nhập chuỗi:')
for ch in S:
    if ch not in [' ','/t']:
        print(ch.upper())
