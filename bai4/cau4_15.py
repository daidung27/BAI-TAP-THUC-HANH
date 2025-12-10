print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
# Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi các từ tiếng Anh, cách nhau bởi dấu cách: ")

# Tách thành danh sách từ
words = s.split()

# Sắp xếp theo thứ tự từ điển
words.sort()

# In ra kết quả
print("Các từ sau khi sắp xếp:")
for word in words:
    print(word)
