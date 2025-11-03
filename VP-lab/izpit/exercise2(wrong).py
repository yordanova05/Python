class Worker():
    def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age
        self.worker_list = []
        self.bonus = self.salary_bonus()
        self.salarybonus = self.salary + self.bonus

    def worker_information(self):
        information = f"{self.worker_num} {self.fname} {self.lname} {self.work_experience_company} {self.salary} {self.age}"
        print(f"({self.worker_num}) {self.fname} {self.lname} ({self.age} years old) works {self.work_experience_company} with salary = {self.salary}, bonus = {self.bonus} => {self.salarybonus}")
        self.worker_list.append(information)

    def salary_bonus(self):
        self.bonus = 0
        if self.work_experience_company >= 5 and self.work_experience_company <= 10:
            self.bonus = self.salary*1.5/100
            return self.bonus
        elif self.work_experience_company > 10:
            self.bonus = self.salary*2/100
            return self.bonus
        elif self.work_experience_company < 5:
            self.bonus = self.salary*0.5/100
            return self.bonus
        

    def search_by_num(self, workers_list, worker_num:str):
        for i in self.worker_list:
            info = i.split(" ")
            if info[0] == worker_num:
                return True
        else:
            return False
        
    def search_by_name_experience(self, fname, work_experience_company:int):
        search_list = []
        for i in self.worker_list:
            info = i.split(" ")
            if info[1] == fname and info[3] == work_experience_company:
                search_list.append(i)
        print(search_list)
            
    def add_worker(self, worker):
        worker_info = worker.worker_information()
        self.worker_list.append(worker_info)
        print(f"New worker was added: {worker.fname} {worker.lname}")

    def remove_worker(self, worker_num):
        for item in self.worker_list:
            id = item.split(" ")
            if id[0] == worker_num:
                self.worker_list.remove[item]
                print("Information deleted!!!")
        print("wrong worker_num!")


number_of_workers = int(input())
workers = []
for x in range(number_of_workers):
    worker_id = input("ID = ")
    worker_fname = input("Name = ")
    worker_lname = input("Last name = ")
    worker_experience = int(input("Experience = "))
    worker_salary = int(input("Salary = "))
    worker_age = int(input("Age = "))

    worker = Worker(worker_id, worker_fname, worker_lname, worker_experience, worker_salary, worker_age)
    workers.append(worker)

workers[0].worker_information()
workers[1].worker_information()
print("------------------")


# 1212
# Yoanna
# Yordanova
# 3
# 2300
# 19
# 1213
# Georgi
# Georgiev
# 3
# 2700
# 21