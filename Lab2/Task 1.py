numbers = [-5, 4, 2, 0, -1, 9]
a = []
count = 0
for i in range(len(numbers)):
    if numbers[i] > 0:
        count = count + 1 
        a.append(numbers[i])
print("Середнє арифметичне", sum(a)/count) 