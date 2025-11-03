import datetime
class FitnessCenter:
    def __init__(self, name):
        self.name = name
        self.users = []  
        self.employees = []
        self.trainers = []
        self.managers = []
        self.daily_visits = {}
        
    def __str__(self):
        users_info = "\n".join([user.__str__() for user in self.users])
        employees_info = "\n".join([employee.__str__() for employee in self.employees])
        trainers_info = "\n".join([trainer.__str__() for trainer in self.trainers])
        managers_info = "\n".join([manager.__str__() for manager in self.managers])
        
        return (f"Name: {self.name}\n"
                f"Users:\n{users_info}\n\n"
                f"Employees:\n{employees_info}\n\n"
                f"Trainers:\n{trainers_info}\n\n"
                f"Managers:\n{managers_info}\n")
        
    def add_user(self, user):
        self.users.append(user)
        
    def add_employee(self,employee):
        self.employees.append(employee)
        
    def add_trainer(self, trainer):
        self.trainers.append(trainer)
    
    def add_manager(self, manager):
        self.managers.append(manager)
        
    def track_daily_visists(self, user_id):
        today = datetime.datetime.now().date()
        if isinstance(user_id, int):
            if today in self.daily_visits:
                self.daily_visits[today]+=1
            else:
                self.daily_visits[today]=1

class Manager:
    def __init__(self, manager_id, fname, lname, organized_events:list):
        self.manager_id = manager_id
        self.fname = fname
        self.lname = lname
        self.organized_events = organized_events
        
    def __str__(self):
        events = ", ".join(map(str,self.organized_events))
        return (f"ID:{self.manager_id}, fname:{self.fname}, lname:{self.lname},organized events:{events}\n")
    
    def organized_event(self, event_name, date):
        event = event_name + f"({date})"
        if event in self.organized_events:
            print("This event exists\n")
        else:
            self.organized_events.append(event)
            
    def manager_information(self):
        return self.__str__()
        
class Student:
    def __init__(self, student_id, fname, lname, monthly_visits):
        self.student_id = student_id
        self.fname = fname
        self.lname = lname
        self.monthly_visits = monthly_visits
        
    def __str__(self):
        return (f"ID:{self.student_id}, fname:{self.fname}, lname:{self.lname}, monthly visits:{self.monthly_visits}")
    
    def early_access_pass(self):
        if self.monthly_visits >= 15:
            print("You have early access pass\n")
        else:
            print("You don't have early access pass\n")
            
    def student_information(self):
        return self.__str__()
        
class RegularUser:
    def __init__(self, user_id, fname, lname, workouts_count):
        self.user_id = user_id
        self.fname = fname
        self.lname = lname
        self.workout_count = workouts_count
        self.vip_status = False
        
    def __str__(self):
        return (f"ID:{self.user_id}, fname:{self.fname}, lname:{self.lname},workout count:{self.workout_count}, vip: {self.vip_status}")
    
    def promote_to_vip(self):
        if self.workout_count >= 100:
            self.vip_status = True
            print("User promoted to VIP status!\n")
    
    def user_information(self):
        return self.__str__()
        
        
class Employee:
    def __init__(self, employee_id, fname, lname):
        self.employee_id = employee_id
        self.fname = fname
        self.lname = lname
        self.evaluations = []
        
    def __str__(self):
        evals = (", ").join(map(str,self.evaluations))
        return (f"ID:{self.employee_id}, fname:{self.fname}, lname:{self.lname}, evaluations:{evals}")
        
    def receive_evaluation(self, manager_id, evaluation_score):
        self.evaluations.append(evaluation_score)
        sum_numbers = 0
        for num in self.evaluations:
            sum_numbers += num
        print(f"Manager({manager_id}): {evaluation_score}")
        print(f"Average: {sum_numbers/len(self.evaluations)}\n")
        
    def employee_information(self):
        return self.__str__()
        
class PersonalTrainer:
    def __init__(self, trainer_id, fname, lname, clients:list):
        self.trainer_id = trainer_id
        self.fname = fname
        self.lname = lname
        self.clients = clients
        
    def __str__(self):
        evals = (", ").join(map(str,self.clients))
        return (f"ID:{self.trainer_id}, fname:{self.fname}, lname:{self.lname}, clients:{evals}")
        
    def organize_group_workout(self, workout_type, max_clients):
        if len(self.clients) >= 5:
            print(f"It was created group for {workout_type} for max {max_clients} clients, now u have {len(self.clients)} clients\n")
        else:
            print(f"Not enough clients to organize a group workout. Current clients: {len(self.clients)}\n")
            
    def trainer_information(self):
        return self.__str__()
        
        
center = FitnessCenter("Fitnes-7")
manager1 = Manager(1234,"Ivan", "Stoimenov", [])
student1 = Student(999,"Georgi", "Georgiev", 20)
regular_user1 = RegularUser(23, "Hristo", "Kisimov", 100)
employee1 = Employee(20, "Mihail", "Drumev")
personal_trainer = PersonalTrainer(1, "Aleksandur", "Georgiev", ["Stoyan","Maria", "Yordan", "Tsvetomir", "Neli"])

center.add_user(student1)
center.add_employee(employee1)
center.add_manager(manager1)
center.add_trainer(personal_trainer)
center.add_user(regular_user1)
center.track_daily_visists(999)
center.track_daily_visists(23)
print(center.__str__())
   
manager1.organized_event("Counting money","03.03.2024")   
print(manager1.manager_information())

print(student1.student_information())
student1.early_access_pass()

print(regular_user1.user_information())
regular_user1.promote_to_vip()

print(employee1.employee_information())
employee1.receive_evaluation(1234,8)

print(personal_trainer.trainer_information())
personal_trainer.organize_group_workout("DeadLift",8)

        
        
    
        
    
    