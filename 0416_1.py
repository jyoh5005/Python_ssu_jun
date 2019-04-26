mylist = [1, 2, 3, 4, 5, 6]
print("a. 첫번째 데이터를 출력하시오. ", mylist[0])
print("b. 두번째부터 다섯번째 까지의 데이터를 리스트 형태로 출력하시오.", mylist[1:5])
print("c. 리스트의 최대값을 출력하시오.", max(mylist))
print("d. 리스트의 최소값을 출력하시오.", min(mylist))
print("e. 리스트의 합을 출력하시오.", end="")
sum = 0
for i in mylist:
    sum += i
print(sum)
print("f. 마지막에서 두번째 데이터를 출력하시오.", mylist[-2])
