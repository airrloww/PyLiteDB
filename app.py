from db_helper import DBHelper

db = DBHelper('database.db')

def main():
    """Main function for the user management program.

    This program allows users to add, delete, update and get users information from the database.
    """
    while True:
        print("\nChoose an option:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Update User")
        print("4. Get User")
        print("5. Exit")
        choice = input("Choose An Option: ")

        if choice == '1':
            email = input("[+] Email address: ")
            # TBD
            # if db.is_user_exists(email):
            #     print(f"[+] customer with Email address: {email} already exists.")
            #     continue
            first = input("[+] First Name: ")
            last = input("[+] last Name: ")
            DOB = input("[+] Date of Birth: ")
            phone = input("[+] Phone Number: ")
            db.add_user(first, last, email, DOB, phone)

        elif choice == '2':
            email = input("[+] Enter customer email address: ")
            db.delete_user(email)

        elif choice == '3':
            old_email = input("[+] Email address: ")
            if not db.is_user_exists(old_email):
                print(f"[+] customer with Email address: '{old_email}' was not found in data.")
            else:
                email = input("[+] New Email address: ")
                first = input("[+] Update First Name: ")
                last = input("[+] Update Last Name: ")
                DOB = input("[+] Update Date of Birth: ")
                phone = input("[+] Update Phone Number: ")
                db.update_user(old_email, email, first, last, DOB, phone)

        elif choice == '4':
            email = input("[+] Enter customer email address: ")
            db.get_user(email)

        elif choice == '5':
            print("[+] Exiting")
            break
        else:
            print("[+] Invalid option. Try again.")

if __name__ == '__main__':
    main()
