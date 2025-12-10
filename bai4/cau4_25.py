print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
# Nhập chuỗi các số, cách nhau bởi dấu phẩy
s = input("Nhập các số (cách nhau bởi dấu phẩy): ")

# Tách và chuyển từng phần tử thành số nguyên
numbers = [int(x) for x in s.split(",")]

# Lọc các số lẻ
odd_numbers = [x for x in numbers if x % 2 != 0]

# In kết quả
print("Các số lẻ là:", ",".join(str(x) for x in odd_numbers))
