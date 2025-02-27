class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def work(self):
        print(f"{self.name} is working as a {self.position}.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying with student ID: {self.student_id}.")

class University:
    def __init__(self):
        self.employees = []
        self.students = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def show_info(self):
        print("University Employees:")
        for employee in self.employees:
            employee.introduce()
            employee.work()
        
        print("\nUniversity Students:")
        for student in self.students:
            student.introduce()
            student.study()

    def remove_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                break 

    def remove_student(self, student_id):
        for stu in self.students:
            if stu.student_id == student_id:
                self.students.remove(stu)
                break  

    def find_person(self, name=None, student_id=None):
        if name:
            for emp in self.employees + self.students:
                if isinstance(emp, Employee) and emp.name == name:
                    return emp
                if isinstance(emp, Student) and emp.name == name:
                    return emp
        elif student_id:
            for stu in self.students:
                if stu.student_id == student_id:
                    return stu
        return None

emp1 = Employee("John", 30, "Professor")
emp2 = Employee("Alice", 40, "Administrator")
stu1 = Student("Bob", 20, "S12345")
stu2 = Student("Charlie", 22, "S67890")

uni = University()
uni.add_employee(emp1)
uni.add_employee(emp2)
uni.add_student(stu1)
uni.add_student(stu2)

uni.show_info()

uni.remove_employee("Alice")
uni.remove_student("S67890")

print("\nUpdated University Info:")
uni.show_info()

person = uni.find_person(name="John")
if person:
    person.introduce()

student = uni.find_person(student_id="S12345")
if student:
    student.study()
