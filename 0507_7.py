from employee import *
fname = "emp.txt"
file = open(fname, "r")

employee_list = []
for line in file:
    words = line.split()
    emp = employee(words[0], words[1])
    employee_list.append(emp)

max_salary = 0
max_name = ""
for x in employee_list:
    salary = int(x.get_salary())
    if salary > max_salary:
        max_salary = salary
        max_name = x.get_name()

print(max_name)
