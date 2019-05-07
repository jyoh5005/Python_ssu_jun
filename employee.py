class employee:
    emp_cnt = 0
    max_salary = 0
    max_name = ""
    def __init__(self, name = "NULL" , salary = 0 ):
        self.name = name
        self.salary = int(salary)
        employee.emp_cnt += 1

        if self.salary > employee.max_salary:
            employee.max_name = self.name
            employee.max_salary = self.salary

    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def get_tot_cnt(self):
        return employee.emp_cnt

    def get_employee_with_max_salary(self):
        return employee.max_name

