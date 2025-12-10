print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
def write_list_to_file(filename, data_list):
    with open(filename, "w") as f:
        for item in data_list:
            f.write(item + "\n")

my_list = ["Python", "Java", "C++", "JavaScript"]
write_list_to_file("output.txt", my_list)
