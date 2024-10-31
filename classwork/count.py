def word_pass_in_parameter_can_be_counted(words):
    newWord = {}
    for letter in words:
        newWord[letter] = words.count(letter)
    return newWord

value = word_pass_in_parameter_can_be_counted('chidinma')
print(value)







