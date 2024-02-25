# task 3
# password generator

import string
import random

def generate_password(length, complexity):
    
    character_sets = {
        1: string.ascii_letters,
        2: string.ascii_letters + string.digits,
        3: string.ascii_letters + string.digits + string.punctuation
    }

   
    password = ''.join(random.choice(character_sets[complexity]) for _ in range(length))

    if complexity == 1:
        if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
            return password
    elif complexity == 2:
        if any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password):
            return password
    elif complexity == 3:
        if any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
            return password

    
    return generate_password(length, complexity)

def main():
  
    length = int(input("Enter the desired password length: "))
    complexity = int(input("Enter the desired password complexity (1-3)<3 is most complex>: "))

    
    password = generate_password(length, complexity)

    
    print("Generated password:", password)

if __name__ == "__main__":
    main()
    

