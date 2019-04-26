file_name = input("입력 파일 이름: ")
file = open(file_name, "r")
table = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1
print(table)
