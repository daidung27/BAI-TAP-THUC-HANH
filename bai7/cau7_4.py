print("Tong doan dai dung")
print("msv:24575202161009")
from itertools import islice

def file_read_from_head(fname, nlines):
    """
    Đọc và in n dòng đầu tiên của tệp.
    """
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            for line in islice(f, nlines):
                print(line, end='')
    except FileNotFoundError:
        print(f"\nKhông tìm thấy tệp: {fname}")
