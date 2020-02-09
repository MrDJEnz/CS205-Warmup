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

                # pass user input
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
    print(" ")

    print("_____________________")
    print("Pizza Primary Table")
    print("--------------------")
    print("State")
    print("PostalCode")
    print("Categories")
    print("PriceRangeMax")
    print("______________________")
    print("Pizza Secondary Table")
    print("---------------------")
    print("City") ## NEED TO UPDATE TO 'pizza' syntax 
    print("Name")
    print("Address")
    print("Latitude")
    print("Longitude")
    print("")


def convert():

    #Checks to see if Pizza.db exists
    # if the the db already exitsted and we ran the create table
    # function, we would return an error

    if path.exists("Pizza.db"):
        print("Err file already exists")
    else:


      # Connecting to the database, this also seems to 
      #crate a Pizza.db file, not quite sure what the black box
      # is doing. .db might be special or it might just be an empty file
      connection = sqlite3.connect("Pizza.db")


      # creates a pointer, not quite sure what it really is
      pointer = connection.cursor()


      # This is where we create a table that will exist inside of 
      # Pizza.db
      connection.execute('''CREATE TABLE PizzaPrimary ([Id] INTEGER PRIMARY KEY,[State] text, [PostalCode] integer,[Categories] text, [PriceRangeMax] integer)''')
          
      connection.execute('''CREATE TABLE PizzaSecondary([Id]INTEGER PRIMARY KEY,[City] text,[Name] integer,[Address] text, [Latitude] integer,[Longitude] integer)''')

      read_PizzaPrim = pd.read_csv (r'PizzaPrim.csv')
      read_PizzaPrim.to_sql('PizzaPrimary', connection, if_exists='append', index = False) 
    # Insert the values from the csv file into the table 'CLIENTS' 

      read_PizzaNotPrim = pd.read_csv (r'PizzaNotPrim.csv')
      read_PizzaNotPrim.to_sql('PizzaSecondary', connection, if_exists='replace', index = False) # Replace the values from the csv file into the table 'COUNTRY'

      #df = pointer.execute("SELECT * FROM PizzaPrim")
      #print(df)

      print("DataBase loaded to LocalHost")

      pointer.close()
      connection.close()

      return 

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
    # if we call printdb before calling newdb, we create an error
    # we also create pizza.db without anything inside of it
 
    # Creates Path variable
    
    if path.exists("Pizza.db"):
      # i was getting indentation errors here
      # so i added a dumb variable
      # python probably doesnt like empty if statments
      # itd be nice if we could figure out if a .notExits function
      # exists, not quite sure how to find the function defintion
      # documentation for SQl3lite in python
      i =3
       # nice the table exits
    else:
      # if db is not set up yet calls connection method

      convert()
       


    # Creates Path variable
    pathDB = "Pizza.db"

    #Creates connection to path variable
    connection = connection_to_db(pathDB)

    #Creates a cursor/pointer. I think this is like  
    # the >>> lines that would be in the SQLlite3 termial
    cursor = connection.cursor()

    #This is where you execute the query
    #Node that this query is surrounded by ""
    # Ive noticed that some SQL commands like the create table
    # above, uses ''' ''', so if your having trouble trying to 
    #experiment doing something, maybe check that first
    cursor.execute("SELECT * FROM PizzaPrimary LIMIT 10;")


    # the cursor doesnt print anything, you need to 
    # fecth the results from the blackbox where ever it s
    results=cursor.fetchall()

    # then you can print the querey variable that you created
    print(results)


    # not sure what this is doing
    connection.commit()

    #Closing connections, online blurb said
    # sometimes if you don't close the connections it crates 
    # problems
    cursor.close()
    connection.close()



# test user command syntax
def parse_english(command):
    # command = "SELECT TEMPORARY_COLOUMN"
    # print(command)
    varlistone = []
    varlistone.append("song")
    varlistone.append("artist")

    varlisttwo = []
    varlisttwo.append("genre")
    varlisttwo.append("bpm")
    
# ~~~~~~~~~~~~ PARSING STRING INPUT (OUTPUTS) VALID SQL ~~~~~~~~~~~~~ #
    #checking if user input contains any (valid) strings
    #split command by spaces and store in list
    commandAlt = re.sub("[^\w]", " ", command).split()

    #iterate through list of user words .. check for invalid input
    for i in range(len(commandAlt)):
        if (commandAlt[i] != "VALID1") and (commandAlt[i] != "VALID2") and (commandAlt[i] != "VALID3"):
            print(commandAlt[i] + " is not a valid command")

    ###OTHERWISE REASSEMBLE/CONVERT VALID COMMANDS TO SQL (MAY BE NEEDED LATER)
    ##commandLinked = " ".join(commandAlt)
        
    #print(command)
    #print(commandAlt)
    #print(commandLinked)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


    
##    # song senorita genre "canadian pop" EXAMPLE
##    if command == "song Senorita genre \"canadian pop\"":
##        print(command)
##        pathDB = "top50.db"
##        connection = connection_to_db(pathDB)
##
##        cursor = connection.cursor()
##        text = command.split(" ")
##        cursor.execute("SELECT * FROM 'MyTable' WHERE Track == 'Senorita' LIMIT 0,30")
##        row = cursor.fetchone()
##        while row is not None:
##            id = row[0]
##            rank = row[1]
##            trackname = row[2]
##            artist = row[3]
##            genre = row[4]
##            bpm = row[5]
##            print("id: " + str(id) + "    rank: " + str(rank) + "    trackname: " + str(trackname) +
##                  "    Artist: " + str(artist) + "    Genre: " + str(genre) + "    BPM: " + str(bpm))
##            row = cursor.fetchone()
##        connection.commit()
##        connection.close()


    # execute sql statement
    # pointer.execute(command)

    ##saves changes to database
    # connection.commit()
            
main()
