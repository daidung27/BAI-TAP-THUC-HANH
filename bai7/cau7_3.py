print("Tong doan dai dung")
print("msv:24575202161009")
def read_file_concise(filename):
    """Đọc toàn bộ nội dung tệp và trả về dưới dạng chuỗi."""
    try:
        # Sử dụng 'with' để đảm bảo tệp được đóng
        with open(filename, 'r', encoding='utf-8') as f:
            # Phương thức .read() đọc toàn bộ tệp
            return f.read()
    except FileNotFoundError:
        return f"Lỗi: Không tìm thấy tệp '{filename}'."
    except Exception as e:
        return f"Lỗi đọc tệp: {e}"
file_name = "a.txt" 

content = read_file_concise(file_name)
print(content)
