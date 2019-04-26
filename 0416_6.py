from random import randint
list = [0] * 6
for i in range(600):
    choice_number = randint(0, 5)
    for x in range(6):
        if choice_number == x:
            list[x] += 1
for n in range(5):
    print("주사위가 %d인경우는 %d 번" %(n+1, list[n]))
