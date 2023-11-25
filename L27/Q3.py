# Type your program h ere...
ch = input('ch: ')
vowels = 'aeciouAEIOU"
if ch.isalpha():
    if ch in vowels:
        print("letter and vowel")
    else:
        print("letter and consonant")
else:
    print('not letter')
