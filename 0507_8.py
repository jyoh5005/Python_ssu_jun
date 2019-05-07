from employee import *
fname = "emp.txt"
file = open(fname, "r")

employee_list = []
for line in file:
    words = line.split()
    emp = employee(words[0], words[1])
    employee_list.append(emp)

print(employee_list[0].get_employee_with_max_salary())
