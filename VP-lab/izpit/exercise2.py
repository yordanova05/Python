class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age

    def worker_information(self):
        return (f"Worker Number: {self.worker_num}, Name: {self.fname} {self.lname}, "
                f"Work Experience: {self.work_experience_company} years, "
                f"Salary: {self.salary}, Age: {self.age}")

    def salary_bonus(self):
        if self.work_experience_company < 5:
            bonus = 0.005
        elif 5 <= self.work_experience_company <= 10:
            bonus = 0.015
        else:
            bonus = 0.02
        return self.salary + (self.salary * bonus)


def search_by_num(workers_list, worker_num):
    for worker in workers_list:
        if worker.worker_num == worker_num:
            return True
    return False


def search_by_name_experience(workers_list, lname, work_experience_company):
    result = [worker for worker in workers_list if worker.lname == lname and worker.work_experience_company == work_experience_company]
    return result


def add_worker(workers_list, worker):
    workers_list.append(worker)


def remove_worker(workers_list, worker_num):
    for worker in workers_list:
        if worker.worker_num == worker_num:
            workers_list.remove(worker)
            print("Information deleted!")
            return
    print("Wrong worker_num!")


workers_list = []

while True:
    action = input("Enter action (add/show/search/remove/exit): ").strip().lower()
    if action == "add":
        worker_num = input("Enter worker number: ")
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        work_experience_company = int(input("Enter work experience (years): "))
        salary = float(input("Enter salary: "))
        age = int(input("Enter age: "))
        worker = Worker(worker_num, fname, lname, work_experience_company, salary, age)
        add_worker(workers_list, worker)

    elif action == "show":
        for worker in workers_list:
            print(worker.worker_information())

    elif action == "search":
        criteria = input("Search by (num/name_experience): ").strip().lower()
        if criteria == "num":
            worker_num = input("Enter worker number: ")
            found = search_by_num(workers_list, worker_num)
            print("Worker found!" if found else "Worker not found.")
        elif criteria == "name_experience":
            lname = input("Enter last name: ")
            work_experience_company = int(input("Enter work experience (years): "))
            found_workers = search_by_name_experience(workers_list, lname, work_experience_company)
            for worker in found_workers:
                print(worker.worker_information())
            if not found_workers:
                print("No workers found with these criteria.")

    elif action == "remove":
        worker_num = input("Enter worker number: ")
        remove_worker(workers_list, worker_num)

    elif action == "exit":
        print("Exiting program.")
        break

    else:
        print("Invalid action. Try again.")
