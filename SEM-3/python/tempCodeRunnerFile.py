num = 12345

num_str = str(num)
new_num = num_str[-1] + num_str[1:-1] + num_str[0]

print(int(new_num))