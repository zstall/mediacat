import os
import psycopg2
import hashlib
import json
from pymediainfo import MediaInfo
from pprint import pprint
from config import config

#psql postgresql://admin:admin@localhost:5432/mediacat -af mediacat.sql

class User:
    """ Class User is the main class to create a user and update the DB"""
    def __init__(self, user_id, fname, lname, phone, email, username, password, date_created, date_updated, admin, super_user, deleted):
        self.user_id = user_id
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.username = username  
        self.password = password
        self.date_created = date_created
        self.date_updated = date_updated 
        self.admin = admin
        self.super_user = super_user
        self.deleted = deleted
    
    def add_user_to_db(self, psswrd):
        query = "INSERT INTO users (fname, lname, phone, email, username, password, date_created, date_updated, user_admin, user_super_user) VALUES(" + "'"+self.fname+"', " + "'"+self.lname+"' ," + "'"+self.phone+"' ," + "'"+self.email+"', " + "'"+self.username+"', " + "crypt('"+psswrd+"', gen_salt('bf', 8)), current_timestamp, current_timestamp, " + self.admin + "," + self.super_user +");"
        print("adding user to db: " + str(self.username) + " with id: " + str(self.user_id))
        query_mediacat(query)

class File:
    ''' This class encompasses files found in a given directory '''
    def __init__(self, file_id, file_sha1, file_name, file_type, file_path, file_size, date_created, date_updated, file_attributes):
        self.file_id = file_id
        self.file_sha1 = file_sha1
        self.file_name = file_name
        self.file_type = file_type
        self.file_path = file_path
        self.file_size = file_size
        self.date_created = date_created
        self.date_updated = date_updated
        self.file_attributes = file_attributes

    def add_file_to_db(self):
         query = "INSERT INTO files (file_sha1, file_name, file_type, file_path, file_size, date_created, date_updated, attributes) VALUES("+"'"+self.file_sha1+"', '"+self.file_name+"', "+"'"+str(self.file_type)+"', "+"'"+self.file_path+"', "+"'"+str(self.file_size)+"', current_timestamp, current_timestamp, "+"'"+self.file_attributes+"'"+") ON CONFLICT DO NOTHING;"
         query_mediacat(query)

    def file_updated(self):
        query = "UPDATE files SET date_updated = '"+self.date_updated+"' WHERE file_sha1 = '"+self.file_sha1+"';"
        query_mediacat(query)

def explore_directory(directory, trace=True):
    for root, sub_dirs, files in os.walk(directory):
        if trace:
            print(
                f"Root: {root}\n"
                f"Sub Directories: {sub_dirs}\n"
                f"Files: {files}\n\n"
            )
        for file in files:
            
            file_plus_path = root + '/' + file
            print(file_plus_path)
            #file_media = runMeadiaInfo(root + '\\' + file)
            
            # For mac/linux
            file_media = MediaInfo.parse(root + '/' + file)
            
            #for windows:
            #file_media = MediaInfo.parse(root + '\\' + file)
            
            general_track = file_media.general_tracks[0]

            if trace:
                print("running on file: " + str(file))
            f = create_file(file, general_track.file_extension, root )

            f.add_file_to_db()

def get_sha1(input_string):
    return hashlib.sha1(input_string.encode()).hexdigest()
             

def create_file(file_name, file_type, file_path):
    # Create unique sha1 value for file

    # For mac linux
    input_string = file_path + '/' + file_name

    # For Windows
    # input_string = file_path + '\\' + file_name

    file_sha1 = get_sha1(input_string)

    general_track = runMeadiaInfo(input_string)
    file_size = general_track.file_size
    date_created = general_track.file_creation_date
    date_updated = general_track.file_last_modification_date
    fjson = json.dumps(general_track.__dict__)


    file = File('', file_sha1 ,file_name, file_type, file_path, file_size, date_created, date_updated, fjson)
    return file


def query_mediacat(query, trace=False):
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL
        if trace:
            print('Connecting to the PostgreSQL database.')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        if trace:
            print("*****************************")
            print("Executing:")
            print(query)
            print("*****************************")
        cur.execute(query)
        conn.commit()

        db_query = cur.fetchall()
        return(db_query)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            cur.close()
            conn.close()

# file is the file path and name 
def runMeadiaInfo(file):
        media_info = MediaInfo.parse(file)
        general_track = media_info.general_tracks[0]
        return(general_track)
    

def updateMediaAttributes(general_track):
    
    return(fjson)
    

def create_user(username, password):
    """ Given a username and password query the db to see if that user exists. If so 
        create a user"""
    u = query_mediacat("select * from users where username = '" + username + "' and password = crypt('" +password +"',password);")

    if u == '':
        print("Incorrect username or password")
        pass
    elif u == []:
        print("Incorrect username or password")
        pass
    else:
        created_user = User(u[0][0],u[0][1],u[0][2],u[0][3],u[0][4],u[0][5],u[0][6],u[0][7],u[0][8],u[0][9],u[0][10],u[0][11])
        return created_user

def create_user_with_id(id):

    u = query_mediacat("select * from users where user_id = '" + id +"';")    
    new_user = User(u[0][0],u[0][1],u[0][2],u[0][3],u[0][4],u[0][5],u[0][6],u[0][7],u[0][8],u[0][9],u[0][10],u[0][11])
    return new_user

def main():

    dir = input(r"please enter a direcotry to walk: ")
    print("Walking dir: " + dir)
    explore_directory(dir)

    #explore_directory(r'C:\Users\zstal\Documents\zstall\MediaCat')
    
    #gr = create_file('text2.txt', 'txt', r'C:\Users\zstal\Documents\zstall\MediaCat\text')
    #gr.file_updated()
    

if __name__ == '__main__':
    main()