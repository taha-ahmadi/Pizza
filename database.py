## Init singleton database
import sqlite3
import os.path

class Database:

    __DB = None
    __conn = None

    @staticmethod
    def getInstance():
        if Database.__DB == None:
            Database()
        return Database.__DB

    # constructor
    def __init__(self):
        if os.path.isfile('database.db'):
            Database.__conn = sqlite3.connect('database.db')
        else:
            Database.__conn = self.database()

        Database.__DB = self
    
    def database(self):
        """ create a database connection to the SQLite database
        :return: Connection object
        """
        try:
            sqlite_connection = sqlite3.connect('database.db')
            sqlite_create_table_query = '''CREATE TABLE todos (
                                        id INTEGER PRIMARY KEY,
                                        do TEXT NOT NULL,
                                        deadline INTEGER,
                                        is_complete BOOLEAN DEFAULT 0,
                                        created_date TIMESTAMP
                                        DEFAULT CURRENT_TIMESTAMP
                                        );'''

            cursor = sqlite_connection.cursor()
            cursor.execute(sqlite_create_table_query)
            sqlite_connection.commit()

            return sqlite_connection

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
            
    
    def query(self, query):
        cur = Database.__conn.cursor()
        cur.execute(query)

        rows = cur.fetchall()

        return rows


    def insert(self, table, data):
        sql_query = "INSERT INTO {table} ({keys}) VALUES ({values})".format(
            table = table,
            keys=','.join([*data]),
            values=','.join(['?']*len(data)))

        cur = Database.__conn.cursor()
        cur.execute(sql_query, tuple(data.values()))
        Database.__conn.commit()
        return cur.lastrowid

    def update(self, table,data , cond):
        sql_query = "UPDATE {table} SET {key} {cond}".format(
            table = table,
            key='= ?, '.join([*data]) + '= ?',
            cond=cond)
        cur = Database.__conn.cursor()
        cur.execute(sql_query, tuple(data.values()))
        Database.__conn.commit()
        return cur.lastrowid


    def delete(self, table, data):
        sql_query = "DELETE FROM {table}  WHERE {data}".format(
            table = table,
            data=' = ?, '.join([*data]) + ' = ?')
        cur = Database.__conn.cursor()
        cur.execute(sql_query, tuple(data.values()))
        Database.__conn.commit()
        return cur.lastrowid
        
    def truncate(self, table):
        sql_query = "DELETE FROM {table}".format(table=table)
        cur = Database.__conn.cursor()
        cur.execute(sql_query)
        Database.__conn.commit()
        return cur.lastrowid
    
    def close(self):
        if (Database.__conn):
                Database.__conn.close()
                print("sqlite connection is closed")