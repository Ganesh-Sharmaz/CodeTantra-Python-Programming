str = str(input("str: "))
sorted_str = sorted(str)
new_list = []
unique_char = set()
current_char = sorted_str[0]
count = 1
for i in range(0,len(sorted_str)):
    if sorted_str[i] == current_char:
        count += 1
    else:
        print(f"'{current_char}'\t{count}")
        current_char = sorted_str[i]
        count = 1
    if sorted_str[i] not in unique_char:
        unique_char.add(sorted_str[i])
        new_list.append(sorted_str[i])
print(f"'{current_char}'\t{count}")
print(new_list)
