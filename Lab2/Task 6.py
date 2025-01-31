string = input("Введіть рядок: ")
count = {} 

for char in string:
    count[char] = count.get(char, 0) + 1  

print("Унікальні символи та кількість їх входжень:")
for char, count in count.items():
    print(f"'{char}': {count}")