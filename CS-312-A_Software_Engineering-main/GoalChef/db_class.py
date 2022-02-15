import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, conn, form, password):
        self.conn = conn
        self.form = form
        self.password = password

    def generate_insert_query(self):
        query = f"""INSERT INTO customer 
                    (first_name, last_name, email_address, password, phone_number, birth_date)
                    VALUES(
                           '{self.form.first_name.data}'
                          ,'{self.form.last_name.data}'
                          ,'{self.form.email_address.data}'
                          ,'{self.password}'
                          ,'{self.form.phone_number.data}'
                          ,'{str(self.form.birth_date.data)}'
                          )"""
        return query

    def insert_customer(self, query):
        cur = self.conn.cursor()
        try:
            cur.execute(query)
            self.conn.commit()
        except Error as e:
            print(e)

    # Checks customer table to see if the email(customers username) exists so we can alert the user that they have an account.
    def check_email_exists(self):
        cur = self.conn.cursor()
        query = f"SELECT user_id FROM customer WHERE email_address = '{self.form.email_address.data}'"
        cur.execute(query)
        result = cur.fetchone()

        # If the email does not exist in the customer table, then this will return false which will allow the user
        # to create their account.
        if result is None:
            return False
        else:
            return True
