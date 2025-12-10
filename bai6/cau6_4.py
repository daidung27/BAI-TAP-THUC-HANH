print("TONG DOAN DAI DUNG")
print("msv:24575202161009")

class py_solution:
    def roman_to_int(self, s):
        rom_val = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        int_val = 0

        for i in range(len(s)):
            # Nếu ký tự hiện tại lớn hơn ký tự trước đó → trừ 2 lần giá trị ký tự trước
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]

        return int_val

# Test theo flowchart
print(py_solution().roman_to_int('MMMD'))
print(py_solution().roman_to_int('C'))
print(py_solution().roman_to_int('IV'))
print(py_solution().roman_to_int('MCMXLIV'))  # ví dụ thêm
