from random import randint
number_list = []
for x in range(10):
    y = randint(0, 100)
    number_list.append(-y)

print("초기 리스트 정보")
print(number_list)
print("-" * 30)

#sorted는 리스트에 지장을 주지 않음
sorted(number_list)
print(number_list)

print("-" * 30)
print(sorted(number_list))


#sort는 리스트에 지장을 줌
print("-" * 30)
number_list.sort()
print(number_list)

print("절댓값 기준으로 정렬")
print("-" * 50)
print(sorted(number_list, key=lambda x: abs(x)))
