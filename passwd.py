import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(service, password):
    """Save the service and password to a file."""
    with open('Passwords.txt', 'a') as file:
        file.write(f"{service}: {password}\n")

def main():
    """Main function to run the password manager."""
    print("Welcome to Password Manager!")
    service = input("Enter the service or website name: ")
    length = int(input("Enter the length of the password to generate: "))

    generated_password = generate_password(length)
    save_password(service, generated_password)

    print(f"Generated password for {service}: {generated_password}")
    print("Password saved successfully in Passwords.txt")

if __name__ == "__main__":
    main()
