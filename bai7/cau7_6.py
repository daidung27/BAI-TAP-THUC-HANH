print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
import sys
import os

def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    with open(fname, encoding='utf8') as f:
        if bufsize > fsize:
            bufsize = fsize - 1
        data = []
        while True:
            iter += 1
            f.seek(fsize - bufsize * iter)
            data.extend(f.readlines())
            if len(data) >= lines or f.tell() == 0:
                print(''.join(data[-lines:]))
                break

file_read_from_tail('a.txt', 2)
