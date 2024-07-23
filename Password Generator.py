import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    character_set = ''
    if use_upper:
        character_set += string.ascii_uppercase
    if use_lower:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation
    
    if not character_set:
        return "No character types selected!"
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        use_upper = input("Include upper case letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lower case letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        if length <= 0:
            print("Password length should be a positive integer.")
            return

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
