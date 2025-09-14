def change_word(word):
    if word == word[::-1]:
        print('Palindrom')
    else:
        print('Palindrom emes')


change_word('казак')
change_word('радар')
change_word('машина')