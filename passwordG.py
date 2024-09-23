import random
import string 

def generate_password(length,use_uppercase, use_lowercase,  use_digits, use_special):
    characters=""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation


    if not characters:
        return "Error! No character types selected."
    
    password= "".join(random.choice(characters)for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length for the password"))

    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    print(f"Generated password: {password}")

if __name__=="__main__":
    main()