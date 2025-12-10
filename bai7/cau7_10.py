print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
def longest_words(text):
    words = text.split()
    max_len = max(len(word) for word in words)
    return [word for word in words if len(word) == max_len]

# Ví dụ sử dụng
text = "tong doan dai dung"
print("Các từ dài nhất:", longest_words(text))
