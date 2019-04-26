file_name = input("입력 파일 이름: ")
file = open(file_name, "r")

def process(w):
    result = ""
    for x in w:
        if x.isalpha():
            result += x
    return result.lower()

words = set()
for line in file:
    linewords = line.split()
    for word in linewords:
        words.add(process(word))

print("사용된 던어의 개수=", len(words))
print(words)
