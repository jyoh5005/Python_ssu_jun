grade_list = []
for i in range(5):
    grade_list.append(int(input("점수를 입력하세요: ")))

average = 0
for i in grade_list:
    average += i
average /= len(grade_list)
print("평균:", average)

student_num = 0
for i in grade_list:
    if i >= average:
        student_num += 1

print("평균 이상의 학생수 =", student_num)


