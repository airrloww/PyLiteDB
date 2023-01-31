import sqlite3

class DBHelper:

    def __init__(self,db_file):
       self.conn = sqlite3.connect(db_file)


    def add_user(self,first, last, email, DOB, phone):
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
        print(f"cutomer {first} {last} has been added.")

 
    def get_user(self, email):
        cur = self.conn.cursor()
        if email:
            cur.execute('''
                SELECT * FROM customers
                WHERE email=?
            ''', (email,))
            data = cur.fetchone()
            if data:
                print(f'''\
customer with '{email}' has the following data: 
[+] First Name: {data[0]}
[+] Last Name: {data[1]}
[+] Email Address: {data[2]}
[+] Date Of Birth: {data[3]} 
[+] Phone Number: {data[4]}''')
            else:
                print(f"no customer with '{email}' was found in database.")
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
        cur = self.conn.cursor()
        cur.execute('''
        UPDATE customers
        SET email=?, first=?, last=?, DOB=?, phone=?
        WHERE email=?
    ''', (email, first, last, DOB, phone, old_email))
        self.conn.commit()
        print(f"customer with Email address: '{old_email}' has been updated.")


    def delete_user(self, email):
        cur = self.conn.cursor()
        cur.execute('''
            DELETE FROM customers
            WHERE email=?
        ''', (email,))
        if cur.rowcount == 0:
            print(f"customer with Email address: '{email}' was not found in customers database.")
        else:
            self.conn.commit()
            print(f"customer with Email address: '{email}' has been deleted.")

    def is_user_exists(self,old_email):
            cur = self.conn.cursor()
            cur.execute('''
            SELECT email FROM customers
            WHERE email=?
        ''', (old_email,))
            return cur.fetchone() != None
