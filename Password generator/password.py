import random
import string

def generate_password(length):
    # Define the character pool
    char_pool = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for the password length
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Password length must be a positive number.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
