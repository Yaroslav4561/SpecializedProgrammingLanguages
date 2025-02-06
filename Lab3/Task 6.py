def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len) if words else ""
    return longest_word

sentence = "Найдовше слово у реченні."
print(find_longest_word(sentence))