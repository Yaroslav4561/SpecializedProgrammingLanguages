class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
       
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(3,4)
vector2 = Vector(5,6)

res_add = vector1 + vector2
print(res_add)

res_sub = vector1 - vector2
print(res_sub)