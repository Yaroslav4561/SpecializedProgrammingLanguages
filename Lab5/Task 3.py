class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

    def __repr__(self):
        return f"{self.name}"

class Student(Human):
    def __init__(self,name, age, university):
        super().__init__(name, age)
        self.university = university
        self.scores = []
    
    def score_list(self, score):
        if 0 <= score <= 5:
            self.scores.append(score)
        else:
            raise ValueError("Оцінка повинна бути в межах від 0 до 5")
        
    def avg_score(self):
        if not self.scores:
            return 0
        else:
          return sum(self.scores) / len(self.scores)

    def __repr__(self):
        return f"Студент({self.name}, Оцінки: {self.scores})"
    
student = Student("Ярослав", 18, "РФКІТ")
student.score_list(4)
student.score_list(5)
student.score_list(4)
print(student)

student.change_name("Влад")
print("Оновлене ім'я:", student.name)

print(student)
print("Середній бал:", student.avg_score())