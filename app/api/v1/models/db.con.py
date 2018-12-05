import psycopg2

class Database:
    def __init__(self):
        self.connect = psycopg2.connect("dbname='incidence_db' user='postgres' host='localhost' password='12345' port='5432'")
        self.connect.autocommit = True
        self.cursor = self.connect.cursor()


    def create_users_table(self):
        create_table = """CREATE TABLE users(
            id serial PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL,
            email VARCHAR(355) UNIQUE NOT NULL,
            createdOn TIMESTAMP NOT NULL)"""
        return self.cursor.execute(create_table)

    def create_incidences_table(self):
        create_table = """CREATE TABLE incidences(
            id serial PRIMARY KEY,
            title VARCHAR(50) NOT NULL,
            record_type VARCHAR(30) NOT NULL,
            location VARCHAR(50) NOT NULL,
            status VARCHAR(50) NOT NULL,
            images VARCHAR(50) NOT NULL,
            videos VARCHAR(50) NOT NULL,
            comment TEXT NOT NULL,
            createdOn VARCHAR(50)
        )"""
        return self.cursor.execute(create_table)


db_con = Database()
db_con.create_users_table()
db_con.create_incidences_table()
