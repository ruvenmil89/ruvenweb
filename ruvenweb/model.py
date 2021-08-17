from ruvenweb import db
import sqlite3


class Feedback(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=False)
    email = db.Column(db.String(length=60), nullable=False, unique=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    @staticmethod
    def create_table(conn):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        create_table_sql = """ CREATE TABLE IF NOT EXISTS feedback (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        description text NOT NULL
                                    ); """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except:
            print("Error")

    @staticmethod
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except:
            print("Error")

        return conn

    @staticmethod
    def select_all_tasks(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM feedback")

        rows = cur.fetchall()

        return rows

    def __repr__(self):
        return f'Item {self.name}'

