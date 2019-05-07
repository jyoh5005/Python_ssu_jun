from employee import *
fname = "emp.txt"
file = open(fname, "r")

employee_list = []
for line in file:
    words = line.split()
    emp = employee(words[0], words[1])
    employee_list.append(emp)
