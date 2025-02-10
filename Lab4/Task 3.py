class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name
    
class Zoo:
    def __init__(self):
        self.animals = []  
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} додано до зоопарку.")
    
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} вилучено із зоопарку")
        else:
            print(f"{animal.name} не знайдено у зоопарку.")
    
    def show_animals(self):
        if self.animals:
            print("Тварини в зоопарку:")
            for animal in self.animals:
                print(f"- {animal.name} ({animal.type})")
        else:
            print("Зоопарк порожній.")

zoo = Zoo()

lion = Animal("Лев", "Сімба")
elephant = Animal("Слон", "Влад")

zoo.add_animal(lion)
zoo.add_animal(elephant)

zoo.show_animals()

zoo.remove_animal(lion)

zoo.show_animals()