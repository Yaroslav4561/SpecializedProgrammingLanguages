sentence = input("Введіть речення: ")
words = sentence.split()
reversed = " ".join(words[::-1])  
res = ""
for char in reversed:
    res = char + res

print("Реверсоване речення:", res)
