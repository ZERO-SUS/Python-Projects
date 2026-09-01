import json
import os

FILE_NAME = "users.json"
logged_in_user = None

# Load users from file
def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# Save users to file
def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f)

def register(users):
    username = input("Enter new username: ")
    if username in users:
        print("❌ Username already exists!")
        return users
    password = input("Enter new password: ")
    users[username] = password
    save_users(users)
    print("✅ Registration successful!")
    return users

def login(users):
    global logged_in_user
    if logged_in_user:
        print(f"⚠️ {logged_in_user} is already logged in!")
        return
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username] == password:
        logged_in_user = username
        print(f"✅ Login successful! Welcome, {username}")
        h=input("Enter your Name:")
        i=int(input("Enter your year of birth:"))
        a=2025-i
        print("your name is ",h)
        print("your age is ",a)
        if a<18:
            print ("your child!!!")
        if a>=18:
            print("your are eligible")


    else:
        print("❌ Invalid username or password")

def logout():
    global logged_in_user
    if logged_in_user:
        print(f"👋 {logged_in_user} logged out successfully!")
        logged_in_user = None
    else:
        print("⚠️ No user is logged in!")

def main():
    users = load_users()
    while True:
        print("\n=== MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Exit")
        
        choice = input("Choose option (1-4): ")
        
        if choice == "1":
            users = register(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            logout()
        elif choice == "4":
            print("🚪 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()
