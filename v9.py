import psycopg2

conn = psycopg2.connect(database="auto", user="posttest", password=1, host="localhost", port=5432)
cursor = conn.cursor()


class Database:
    def __init__(self):
        self.connection = conn
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, full_name):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id',full_name) VALUES (?,?)", (user_id, full_name))

    def get_all_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, full_name FROM users").fetchall()

    def create_table(self):
        with self.connection:
            return cursor.execute('''
    CREATE TABLE IF NOT EXISTS users_datas (
        id serial PRIMARY KEY ,
        user_id INTEGER NOT NULL,
        full_name TEXT NOT NULL)''')

    def close_connection(self):
        with self.connection:
            try:
                self.cursor.close()
                print("Connection closed successfully")
            except psycopg2.Error as e:
                print("Error while closing connection:", e)


if __name__ == "__main__":
    database = Database()
    database.create_table()
    database.close_connection()
