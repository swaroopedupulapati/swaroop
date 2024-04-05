import random
import string

def generate_password(length=12):
    """Generate a random password with the specified length."""
    # Define the character sets to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("Welcome to the Password Generator")
    print("===============================")
    
    # Prompt the user for the desired length of the password
    length = int(input("Enter the length of the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
