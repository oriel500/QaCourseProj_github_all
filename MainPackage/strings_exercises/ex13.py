sentence = input("Enter sentence: ")
letter1 = input("Enter letter: ")
new_sentence = ""

for letter in sentence:
    if letter1 == letter:
        new_sentence += letter.capitalize()
    else:
        new_sentence += letter

print(new_sentence)
