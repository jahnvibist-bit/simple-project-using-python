#import datetime
#import pytz
def save(name, age, email, password, status):
    '''
    india_timezone = pytz.timezone('Asia/Kolkata')
    v=datetime.datetime.now(india_timezone)
    '''
    data = ( name + "," + str(age) + "," + email + "," + str(password) + "," + status + "\n" )
    with open("info.txt", "a") as file:
        file.write(data)


def read_data():
    with open("info.txt", "r") as file:
        print("\n--- File Data ---")
        print(file.read())


def registration():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age > 18:
        email = input("Enter your email (eg. abc@gmail.com): ")
        password = input("Set password (in digits): ")
        while True:
            rpass = input("Re-enter password for confirmation: ")
            if rpass == password:
                print(f"\n{name}, your registration is successful!")
                save(name, age, email, password, "Registered")
                break
            else:
                print("\nPasswords do not match! Try again.")
    else:
        print("\nRegistration allowed only for age above 18.")


def login():
    attempt = 1
    max_attempts = 3
    while attempt <= max_attempts:
        choice = int(input("\n1. Login by Email & Password\n2. Login by Username\nEnter your choice: "))
        if choice == 1:
            mail = input("Enter your email: ")
            epass = input("Enter your password: ")
            found = False
            with open("info.txt", "r") as file:
                for line in file:
                    name, age, email, password, status = line.strip().split(",")
                    if mail == email and epass == password:
                        print(f"\nWelcome back {name}! You've logged in successfully.")
                        save(name, age, email, password, "Logged In")
                        found = True
                        break
            if found:
                return
            else:
                print("Incorrect email or password.")
                attempt += 1

        elif choice == 2:
            uname = input("Enter your name: ")
            epass = input("Enter your password: ")
            with open("info.txt", "r") as file:
                for line in file:
                    name, age, email, password, status = line.strip().split(",")
                    if uname == name and epass == password:
                        user = name[:3] + password[:3]
                        print(f"\nYour generated username is: {user}")
                        user_input = input("Enter your generated username: ")
                        if user_input == user:
                            print(f"\n{name}, you've logged in successfully!")
                            save(name, age, email, password, "Logged In")
                            return
                        else:
                            print("Incorrect username.")
                            break
            attempt += 1
        else:
            print("Invalid choice. Please select 1 or 2.")
            attempt += 1

    print("\nMaximum login attempts exceeded!")


# Main program
print("********* Welcome To My Portal *********")
num = 0
while num != 4:
    num = int(
        input(
            "\n*OPTIONS AVAILABLE* \n1. Register \n2. Login \n3. Read Data File \n4. Exit \nEnter your choice: "
        )
    )
    match num:
        case 1:
            registration()
        case 2:
            login()
        case 3:
            read_data()
        case 4:
            print("********* Thank you for visiting my portal! *********")
        case _:
            print("Invalid input! Try again.")
