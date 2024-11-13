
import psycopg2
import os
from MediaCat import File, explore_directory, User
from config import config

def executeScript(script):
    """" Fill out laters, yes I'm lazy :) """

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        
        # execute script
        print("Execute Script " + str(script))

        os.system("psql -U admin -d mediacat -a -f " + script)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            print('Queries Executed Succesfully.') 

def executeInserts(fn, ln, ph, eml, usrnm, psswrd, created, updated, usr_admin, usr_super_user):
    """" Fill out laters, yes I'm lazy :) """

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        query = "INSERT INTO users (fname, lname, phone, email, username, password, date_created, date_updated, user_admin, user_super_user) VALUES("+fn+","+ln+","+ph+","+eml+","+usrnm+","+psswrd+","+created+","+updated+","+usr_admin+","+usr_super_user+");"

        # create a cursor
        cur = conn.cursor()
        print('Executing query:')
        print(query)
        cur.execute(query)
        conn.commit()

        db_query = cur.fetchone()
        print(db_query)

         # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            print('Queries Executed Succesfully.')

def connect(query="SELECT version();",script=False):
    """ function to connect to the DB and run scripts or queries """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        
        # execute statement
        if(not script):
            print('Executing query:')
            print(query)
            cur.execute(query)

            conn.commit()
            db_query = cur.fetchone()
            print(db_query)
        else:
            print("Execute Script")
            os.system("psql -U admin -d mediacat -a -f " + query)

    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            print('Queries Executed Succesfully.')    


def main():

    executeScript('mediacat.sql')

    users=[
        ["admin", "admin", "5555555555", "admin@noreply.com", "admin", "admin","current_timestamp","current_timestamp", "True", "True"],
        ["admin2", "admin2", "5555555555", "tester1@noreply.com", "admin2", "admin","current_timestamp","current_timestamp", "True", "False"],
        ["test1", "tester1", "5555555555", "tester1@noreply.com", "tester1", "password","current_timestamp","current_timestamp", "True", "False"],
        ["test2", "tester2", "5555555555", "tester1@noreply.com", "tester2", "password","current_timestamp","current_timestamp", "True", "False"],
        ["test3", "tester3", "5555555555", "tester1@noreply.com", "tester3", "password","current_timestamp","current_timestamp", "True", "False"],
        ["test4", "tester4", "5555555555", "tester1@noreply.com", "tester4", "password","current_timestamp","current_timestamp", "True", "False"],
        ["test5", "tester5", "5555555555", "tester1@noreply.com", "tester5", "password","current_timestamp","current_timestamp", "True", "False"],
        ["test6", "tester6", "5555555555", "tester1@noreply.com", "tester6", "password","current_timestamp","current_timestamp", "True", "False"],
        ["test7", "tester7", "5555555555", "tester1@noreply.com", "tester7", "password","current_timestamp","current_timestamp", "True", "False"],
        ["test8", "tester8", "5555555555", "tester1@noreply.com", "tester8", "password","current_timestamp","current_timestamp", "True", "False"]
    ]

    for i in users:
        u = User('',i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],'False') 
        u.add_user_to_db(u.password)
        print("Added user: " + u.username)

    explore_directory('/mediacatapp/test')




if __name__ == '__main__':
    main()
