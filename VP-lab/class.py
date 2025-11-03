class Person():
    def __init__(self, name, fname, age, nationality):
        self.name = name
        self.fname = fname
        self.age = age
        self.nat = nationality

    def print_information(self):
        print(f"{self.name} {self.fname} is {self.nat}.\nYou are {self.age} years old.\n")


class Student(Person):
    def __init__(self, name, fname, age, nationality, university, graduation_year):
        Person.__init__(self, name, fname, age, nationality)
        self.uni = university
        self.graduation = graduation_year

    def print_grad(self):
        print(f"You studied in {self.uni} and u graduated in {self.graduation}")


class Lecturer(Person):
    def __init__(self, name, fname, university, experience):
        Person.__init__(self, name, fname, age= None, nationality=None)
        self.uni = university
        self.exp = experience

    def print_lecturer(self):
        print(f"{self.name} {self.fname} is {self.exp}")


person1 = Person("Yordan", "Yordanov", 23, "bulgarian")
person1.print_information()

person2 = Person("Milena", "Georgieva", 20, "german")
person2.print_information()

# name = input("Name: ")
# fname = input("Middlename: ")
# age = int(input("Age: "))
# nationality = input("Nationality: ")
# print()

# person3 = Person(name,fname,age,nationality)
# person3.print_information()

person4 = Student("Maria","Ivanova" , 24, "american", "PMG ""Vasil Drumev""", 2022)
person4.print_grad()

person5 = Lecturer("Georgi", "Ivailov", "Technical university", "math teacher")
person5.print_lecturer()



