# CS205 Warm up (Team 8)
# January 27, 2020

# possibly needed module for later sql functionality
import sqlite3
import pandas as pd
import os.path
from os import path
import re

def main():
    # initialize database & parser
    myinput = ""
    
    # #creates bridge to database
    # connection = sqlite3.connect("top50.db")
    #
    # #creates "point of command"
    # pointer = connection.cursor()

    #
    
    ###################### JD 
    #connection = sqlite3.connect("Pizza.db")

    #pointer = connection.cursor()
    #TODO: need to handle Tables being created only once

    #connection.execute('''CREATE TABLE PizzaPrimary ([Id] INTEGER PRIMARY KEY,[State] text, [PostalCode] integer,[Categories] text, [PriceRangeMax] integer)''')
          
    #connection.execute('''CREATE TABLE PizzaSecondary([Id]INTEGER PRIMARY KEY,[City] text,[Name] integer,[Address] text, [Latitude] integer,[Longitude] integer)''')

    #read_PizzaPrim = pd.read_csv (r'PizzaPrim.csv')
    #read_PizzaPrim.to_sql('PizzaPrimary', connection, if_exists='append', index = False) 
    # Insert the values from the csv file into the table 'CLIENTS' 

    #read_PizzaNotPrim = pd.read_csv (r'PizzaNotPrim.csv')
    #read_PizzaNotPrim.to_sql('PizzaSecondary', connection, if_exists='replace', index = False) # Replace the values from the csv file into the table 'COUNTRY'
    
    ########################### JD
    
    
    
    
    
    
    
    while(myinput != "quit"):
        try:
            # gets user input
            myinput = str(input("Waiting for user input: "))

            # checks if user asks for commands help
            if (myinput == "help"):
                help()
            elif (myinput == "quit"):
                #disconnects from database and ends program
                # connection.close()
                break
            elif myinput == "newdb":
                convert()
            elif myinput == "printdb":
                printdb()

            else:
                # listen for sql input
                command = myinput
                parse_english(command)

            # print(myinput)
        except (RuntimeError):
            print("palceholder error")
        #except (sqlite3.OperationalError):
        #    print("SQL Syntax Error")


        

# displays list of commands
def help():
    print("help screen ... example command")
    print("FORMAT TO PARSE DATA AS FOLLOWS: ...")


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

# Connection to the database
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



def parse_english(command):
    # command = "SELECT TEMPORARY_COLOUMN"
    # print(command)
    varlistone = []
    varlistone.append("song")
    varlistone.append("artist")

    varlisttwo = []
    varlisttwo.append("genre")
    varlisttwo.append("bpm")

    # song senorita genre "canadian pop"
    if command == "song Senorita genre \"canadian pop\"":
        print(command)
        pathDB = "top50.db"
        connection = connection_to_db(pathDB)

        cursor = connection.cursor()
        text = command.split(" ")
        cursor.execute("SELECT * FROM 'MyTable' WHERE Track == 'Senorita' LIMIT 0,30")
        row = cursor.fetchone()
        while row is not None:
            id = row[0]
            rank = row[1]
            trackname = row[2]
            artist = row[3]
            genre = row[4]
            bpm = row[5]
            print("id: " + str(id) + "    rank: " + str(rank) + "    trackname: " + str(trackname) +
                  "    Artist: " + str(artist) + "    Genre: " + str(genre) + "    BPM: " + str(bpm))
            row = cursor.fetchone()
        connection.commit()
        connection.close()


    # execute sql statement
    # pointer.execute(command)

    ##saves changes to database
    # connection.commit()
            
main()
