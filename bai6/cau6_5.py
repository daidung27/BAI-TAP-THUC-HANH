print("TONG DOAN DAI DUNG")
print("msv:24575202161009")

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


# -------------------------
# Chạy thử theo đề bài
# -------------------------
print(py_solution().reverse_words("hello .py"))
