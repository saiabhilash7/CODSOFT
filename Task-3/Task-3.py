import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for complexity.")
        return None
    
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    # Ensure the password contains at least one character from each set
    all_characters = lower + upper + digits + punctuation
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue

        password = generate_password(length)
        if password:
            print(f"Generated password: {password}")
        
        another = input("Generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting the password generator. Stay safe!")
            break

if __name__ == "__main__":
    main()
