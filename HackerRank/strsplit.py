string = input()
substring = input()
count = 0
index = 0
while 0 <= index:
    index = string.find(substring)

    if index == -1:
        break
    string = string[index+1:]
    count += 1
print(count)