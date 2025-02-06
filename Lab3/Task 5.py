def capitalize_words(s):
    words = s.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return ' '.join(capitalized_words)

input_string = "приклад тексту"
output_string = capitalize_words(input_string)
print(output_string)  
