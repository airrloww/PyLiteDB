import sqlite3

class DBHelper:
    """
    A database helper class to add, retrieve, update, and delete customers from an SQLite database.
    
    Parameters:
        db_file (str): the database file to be connected to.

    Attributes:
        conn (obj): sqlite3 connection object to the database.
    """
    def __init__(self,db_file):
        """
        Connects to the database file.
        
        :param db_file: the name of the database file
        """
        self.conn = sqlite3.connect(db_file)


    def add_user(self,first, last, email, DOB, phone):
        """
        Add a new customer record to the customers table in the database.
        
        :param first: first name of the customer
        :param last: last name of the customer
        :param email: email address of the customer
        :param DOB: date of birth of the customer
        :param phone: phone number of the customer
        """
        cur = self.conn.cursor()
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS customers (
                    first VARCHAR(30),
                    last VARCHAR(30),
                    email VARCHAR(120) UNIQUE,
                    DOB DATETIME,
                    phone VARCHAR(10) UNIQUE
        )''')
        cur.execute('''
            INSERT INTO customers Values (:first, :last, :email, :DOB, :phone)
        ''', (first, last, email, DOB, phone))
        self.conn.commit()
        print(f"[+] cutomer {first} {last} has been added.")

 
    def get_user(self, email):
        """
        Retrieve customer data from the customers table in the database.
        
        :param email: email address of the customer (required)
        :return: a tuple with customer data if customer with email exists.
        """
        cur = self.conn.cursor()
        if email:
            cur.execute('''
                SELECT * FROM customers
                WHERE email=?
            ''', (email,))
            data = cur.fetchone()
            if data:
                print(f'''\
[+] customer with '{email}' has the following data: 
[+] First Name: {data[0]}
[+] Last Name: {data[1]}
[+] Email Address: {data[2]}
[+] Date Of Birth: {data[3]} 
[+] Phone Number: {data[4]}''')
            else:
                print(f"[+] no customer with '{email}' was found in database.")
        else:
            cur.execute('''
                SELECT * FROM customers
            ''')
            data = cur.fetchall()
            print("All data:")
            for d in data:
                print(f"{d[0]}: {d[1]}: {d[2]}: {d[3]}: {d[4]}")

        return data

    
    def update_user(self, old_email, email, first, last, DOB, phone):
        """
        Update customer data in the customers table in the database.
        
        :param old_email: the original email address of the customer
        :param email: the new email address of the customer
        :param first: the new first name of the customer
        :param last: the new last name of the customer
        :param DOB: the new date of birth of the customer
        :param phone: the new phone number of the customer
        """
        cur = self.conn.cursor()
        cur.execute('''
        UPDATE customers
        SET email=?, first=?, last=?, DOB=?, phone=?
        WHERE email=?
    ''', (email, first, last, DOB, phone, old_email))
        self.conn.commit()
        print(f"[+] customer with Email address: '{old_email}' has been updated.")


    def delete_user(self, email):
        """
        Delete customer data from the customers table in the database.
        
        :param email: email address of the customer
        """
        cur = self.conn.cursor()
        cur.execute('''
            DELETE FROM customers
            WHERE email=?
        ''', (email,))
        if cur.rowcount == 0:
            print(f"[+] customer with Email address: '{email}' was not found in customers database.")
        else:
            self.conn.commit()
            print(f"[+] customer with Email address: '{email}' has been deleted.")

    def is_user_exists(self,old_email):
        """
        Check if customer with email address exists in the customers table in the database.
        
        :param old_email: email address of the customer
        :return: True if customer exists, False otherwise.
        """
        cur = self.conn.cursor()
        cur.execute('''
        SELECT email FROM customers
        WHERE email=?
    ''', (old_email,))
        return cur.fetchone() != None
