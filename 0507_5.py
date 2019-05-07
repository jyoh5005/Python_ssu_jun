class employee:
    emp_cnt = 0
    def __init__(self, name = "NULL" , salary = 0 ):
        self.name = name
        self.salary = salary
        employee.emp_cnt += 1
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def get_tot_cnt(self):
        return employee.emp_cnt
