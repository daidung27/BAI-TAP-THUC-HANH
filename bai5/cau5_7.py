print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
import numpy as np

# Khai báo kiểu dữ liệu cho từng trường
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Danh sách sinh viên
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

# Tạo mảng cấu trúc
students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

# Sắp xếp mảng theo chiều cao (height)
print("\nSort by height:")
print(np.sort(students, order='height'))
