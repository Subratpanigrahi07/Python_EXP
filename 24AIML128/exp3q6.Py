#WRITE A PROGRAM TO INPUT AN ALPHABET AND CHECH WHEATHER IT IS VOWEL OR CONSTANT


ch = input("Enter an alphabet: ")

if len(ch) == 1 and ch.isalpha():
    ch = ch.lower()
    
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("It is a Vowel.")
    else:
        print("It is a Consonant.")
else:
    print("Invalid input! Please enter a single alphabet.")