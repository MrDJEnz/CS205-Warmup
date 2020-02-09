import sqlite3
import pandas as pd
import os.path
from os import path
import re
def convert():

    if path.exists("top50.db"):
        print("Err file already exists")
    else:
        # load data
        df = pd.read_csv('top50.csv')

        # strip whitespace from headers
        df.columns = df.columns.str.strip()

        con = sqlite3.connect("top50.db")

        # drop data into database
        df.to_sql("MyTable", con)

        con.close()

        print("Database successfully created.")

def connection_to_db(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = sqlite3.connect(db_file)

    return conn

def printdb():
    pathDB = "top50.db"
    connection = connection_to_db(pathDB)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM 'MyTable' LIMIT 0,30")
    row = cursor.fetchone()
    while row is not None:
        id = row[0]
        rank = row[1]
        trackname = row[2]
        print("id: " + str(id) + "    rank: " + str(rank) + "    trackname: " + str(trackname))
        row = cursor.fetchone()

    connection.commit()

def basic_english_to_sql():
    loop = True
    while loop:
        usrinput = input("\nPlease enter information for pizza: ")

        # ~~~~THIS PORTION SPLITS USER INPUT INTO LISTS OF WORDS.. ALSO CHECKS FOR INVALID ~~~#
        #split up string into 
        usrinputAlt = re.sub("[^\w]", " ", usrinput).split()

        #iterate through list of user words .. check for invalid input
        for i in range(len(usrinputAlt)):
            if (usrinputAlt[i] != "VALID1") and (usrinputAlt[i] != "VALID2") and (usrinputAlt[i] != "VALID3"):
                print(usrinputAlt[i] + " is not a valid command")
                
        #OTHERWISE REASSEMBLE/CONVERT VALID COMMANDS TO SQL (MAY BE NEEDED LATER)
        usrInputLinked = " ".join(usrinputAlt)

        print(usrinput)
        print(usrinputAlt)
        print(usrInputLinked)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        if usrinput == "help":
            print("\nOptions for user:")
            print("1) Type ' ____ 'for ____.")
            print("2) Type 'newdb' for new db creation.")
            print("3) Type 'help' for this menu.")
            print("4) Type 'quit' to exit.\n")
        elif usrinput == "printdb":
            printdb()
        elif usrinput == "newdb":
            convert()
        elif usrinput == "____":
            #TODO
            print("Do stuff")
        elif usrinput == "quit":
            print("Quitting the program :)")
            loop = False
        else:
            print(usrinput + " is invalid syntax. Please type 'help' for more info.")


basic_english_to_sql()
