a = input("Введіть рядок: ").replace(" ", "").lower()

if a == a[::-1]:
    print("Введений рядок - паліндром")
else:
    print("Введений рядок не є паліндром.")
