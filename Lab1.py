import math
# 1

age = int(input("Введіть вік: "))
result = age * 365
print("Ваш вік у днях: ", result)

#2
a = float(input("Введіть масу тіла (кг): "))
b = float(input("Введіть прискорення (км/год): "))
result = a * bР
print("Сила яку приклали до тіла: ", result)
#3
a = int(input('Введіть перше число квадратного рівняння: '))
b = int(input('Введіть друге число квадратного рівняння: '))
c = int(input('Введіть третє число квадратного рівняння: '))
diskr = b**2 - 4 * a * c
if diskr > 0:
  res1 =(-b + (diskr/2))/2*a
  res2 =(-b - (diskr/2))/2*a
  print("Перший корінь: ", res1, "Другий корінь: ", res2)
elif diskr == 0:
  res = -b / 2*a
  print("Корінь: ", res)
else:
  print("Корені рівняння відсутні")

#4
print("Виберіть спосіб обчислення площі трикутника:")
print("1. Формула Герона (за трьома сторонами)")
print("2. За основою та висотою")
print("3. За двома сторонами та кутом між ними")

choice = input("Введіть номер вибраного способу (1, 2 або 3): ")

try:
    if choice == "1":
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))
        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"Площа трикутника за формулою Герона: {area:.2f}")
        else:
            print("Помилка: такі сторони не утворюють трикутник.")

    elif choice == "2":
        base = float(input("Введіть довжину основи: "))
        height = float(input("Введіть висоту: "))
        if base > 0 and height > 0:
            area = 0.5 * base * height
            print(f"Площа трикутника за основою та висотою: {area:.2f}")
        else:
            print("Помилка: основа та висота повинні бути додатними числами.")

    elif choice == "3":
        a = float(input("Введіть довжину першої сторони: "))
        b = float(input("Введіть довжину другої сторони: "))
        angle = float(input("Введіть кут між ними (у градусах): "))
        if a > 0 and b > 0 and 0 < angle < 180:
            angle_radians = math.radians(angle)
            area = 0.5 * a * b * math.sin(angle_radians)
            print(f"Площа трикутника за двома сторонами і кутом: {area:.2f}")
        else:
            print("Помилка: сторони повинні бути додатними, а кут — між 0 і 180 градусами.")

    else:
        print("Невірний вибір. Будь ласка, введіть 1, 2 або 3.")

except ValueError:
    print("Помилка: введіть числові значення.")

#5
a = 5
b = 9
c = 2
print("Максимальне з наведених чисел: ", max(a, b, c), "\nМінімальне з наведених чисел: ", min(a, b, c))

#6
a = int(input("Введіть число: "))
if 1<=a<=100:
  i = 1
  res = 0
  for i in range(1, a+1):
    res = i + res
  print(res)

# 7
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
res = []
for i in range(a, b + 1):
    res.append(i)
print(res)

# 8
a = int(input('Введіть число: '))
res = a - 1
print("Попереднє число:", res)
