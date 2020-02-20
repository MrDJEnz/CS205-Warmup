# CS205 Warm up (Team 8)
# January 27, 2020
'''
Authors:
Nick Corwin
Jacob Drake
Duncan Enzmann
Kevin Yeung
'''


import sqlite3
import pandas as pd
import os.path
from os import path
import re
import shlex
validCommands = ["State", "StateCode", "PostalCode", "Categories", "PriceRangeMax", "City", "Name", "Address", "Coordinates"]

def main():
    # initialize database & parser
    myinput = ""
    
    # #creates bridge to database
    # connection = sqlite3.connect("top50.db")
    #
    # #creates "point of command"
    # pointer = connection.cursor()
    
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
            elif myinput == "load data":
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

# displays list of commands
def help():
    
    print("Welcome to the help screen")
    print("FORMAT TO PARSE DATA AS FOLLOWS: ...")
    
    print("If you haven't run load data yet...")
    print("you need to type, load data, enter")
    print("before any of the commands below")
    print("will work")
    
    print(" ")
    print("Create a new database:  load data")
    print("_____________________")
    print("Pizza Secondary Table (Table 1)")
    print("---------------------")
    print("City")
    print("Name")
    print("Address")
    print("Latitude")
    print("Longitude")
    print("StateCode")
    print("")    
  
    print("______________________")
    print("Pizza Primary Table (Table 2")
    print("--------------------")
    print("State")
    print("PostalCode")
    print("Categories")
    print("PriceRangeMax")
    print("______________________")
    print("Below are examples of valid commands")
    print("---------------------")
    print("Address State \"NY\"")
    print("Name City Cincinnati")
    print("Name State AZ City Phoenix")
    print("Table1 Table1 option")
    print("Table2 Table1 option")
    print("Table2 Table1 option Table2 option")
    print("---------------------")
    
   

def convert():

    #Checks to see if Pizza.db exists
    # if the the db already exitsted and we ran the create table
    # function, we would return an error

      if path.exists("Pizza.db"):

        os.remove("Pizza.db")
        print("file overwritten")


      # Connecting to the database, this also seems to 
      #crate a Pizza.db file, not quite sure what the black box
      # is doing. .db might be special or it might just be an empty file
      connection = sqlite3.connect("Pizza.db")


      # creates a pointer, not quite sure what it really is
      pointer = connection.cursor()


      # This is where we create a table that will exist inside of 
      # Pizza.db
      connection.execute('''CREATE TABLE PizzaPrimary ([Id] INTEGER PRIMARY KEY,[State] text, [PostalCode] integer,[Categories] text, [PriceRangeMax] integer)''')
          
      connection.execute('''CREATE TABLE PizzaSecondary([Id]INTEGER PRIMARY KEY,[City] text,[Name] integer,[Address] text, [Coordinates] text,[StateCode] text)''')

      read_PizzaPrim = pd.read_csv (r'PizzaPrim.csv')
      read_PizzaPrim.to_sql('PizzaPrimary', connection, if_exists='append', index = False) 
    # Insert the values from the csv file into the table 'CLIENTS' 

      read_PizzaNotPrim = pd.read_csv (r'PizzaNotPrim.csv')
      read_PizzaNotPrim.to_sql('PizzaSecondary', connection, if_exists='replace', index = False) # Replace the values from the csv file into the table 'COUNTRY'

      print("DataBase loaded to LocalHost")

      pointer.close()
      connection.close()

      return 


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
  
  if path.exists("Pizza.db"):
    i = 3
  else:
    convert()   


  try:
    
# ~~~~~~~~~~~~ PARSING STRING INPUT (OUTPUTS) VALID SQL ~~~~~~~~~~~~~ #
    #checking if user input contains any (valid) strings
    #split command by spaces and store in list
    #commandAlt = re.sub("[^\w]", " ", command).split()
    # Using Shlex Library to clean up the regex parser to include quotations
    commandAlt = shlex.split(command)

# ~~~~~~~~~~~~ PARSING STRING INPUT (OUTPUTS) VALID SQL [UPDATED] ~~~~~~~~~~~~~ #

    # print(commandAlt)

    commandDB = []
    commandUsr = []

    # Check if the regex split command is a DB command or user input inside the columns
    for i in commandAlt:
        if i not in validCommands:
            commandUsr.append(i)
        else:
            commandDB.append(i)
    # If there are no DB commands then there is nothing to query
    if len(commandDB) == 0:
        print("Incorrect Parse please type 'help' for more information...")
    else:
        sql_lookup_state(commandDB, commandUsr, commandAlt)
    # Throw an error
  except:
    print("ERROR")
    print("--------------------------------------------")
    print("Please enter correct psudo query formatting")
    print("Type help and then press enter")
    print("To see a list of valid commands")
    print("make sure you have run load data first")
    print("type load data, enter to create database")
    print("--------------------------------------------\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# State to run sqlite3 on
'''

Inputs: Database Commands, User Commands
Does: Runs SQL on english commands and converts into a SQL standard lookup
Prints: The result of the lookup

'''
def sql_lookup_state(commandDB, commandUsr, commandTotal):

  try:
    # Gets the user and DB commands, and loads the table names
    list_unique_vars_db = commandDB
    list_unique_vars_usr = commandUsr
    tables = ["PizzaPrimary", "PizzaSecondary"]
    conn = connection_to_db("Pizza.db")
    c = conn.cursor()
    list_of_results = []

    # Column names in each database
    table1 = ["State", "PostalCode", "Categories", "PriceRangeMax"]
    table2 = ["City", "Name", "Address", "Coordinates", "StateCode"]

    # Determine which table to be looking at for the database commands
    if str(list_unique_vars_db[0]) in table2:
        variable = "snd."
    elif str(list_unique_vars_db[0]) in table1:
        variable = "prim."

    if str(list_unique_vars_db[1]) in table2:
        variable1 = "snd."
    elif str(list_unique_vars_db[1]) in table1:
        variable1 = "prim."

    if len(list_unique_vars_db) == 3:
        if (list_unique_vars_db[2] in table2):
            variable2 = "snd."
        else:
            variable2 = "prim."

    # If we only have 2 DB commands i.e. Name State AR
    # What is the name of the restaurant(s) in the state of Arkansas
    # Run one of three cases
    if len(commandDB) < 3:

        # If both commands are in table 1
        if (commandDB[0] in table1) and (commandDB[1] in table1):
            for row in c.execute("SELECT " + str(list_unique_vars_db[0]) +
                                 " FROM " + tables[0] +
                                 " WHERE " + str(list_unique_vars_db[1]) + "='" + str(list_unique_vars_usr[0]) + "'"):

                if row[0] not in list_of_results:
                    list_of_results.append(row[0])


        # If both commands are in table 2
        elif (commandDB[0] in table2) and (commandDB[1] in table2):
            for row in c.execute("SELECT " + str(list_unique_vars_db[1]) +
                                 " FROM " + tables[1] +
                                 " WHERE " + str(list_unique_vars_db[0]) + "='" + str(list_unique_vars_usr[0]) + "'"):

                if row[0] not in list_of_results:
                    list_of_results.append(row[0])

        else:
        # If the commands are split between the two tables
            for row in c.execute(
                    "SELECT " + variable + str(list_unique_vars_db[0]) + ", " + variable1 + str(list_unique_vars_db[1]) +
                    " FROM " + tables[0] + " AS prim " +
                    " JOIN " + tables[1] + " AS snd " + " ON " + "prim.State=snd.StateCode" +
                    " WHERE " + variable1 + str(list_unique_vars_db[1]) + "= " + "'" + str(list_unique_vars_usr[0]) + "'"):

                if row[0] not in list_of_results:
                    list_of_results.append(row[0])

    # If the user asks for 3 commands i.e.
    # Name State AR PostalCode 72120
    # What is the name of the restaurant(s) in the State of Arkansas where the postalcode is 72120
    elif len(commandDB) == 3:
        for row in c.execute(
                "SELECT " + variable + str(list_unique_vars_db[0]) + ", " + variable1 + str(list_unique_vars_db[1]) +
                " FROM " + tables[0] + " AS prim " +
                " JOIN " + tables[1] + " AS snd " + " ON " + "prim.State=snd.StateCode" +
                " WHERE " + variable1 + str(list_unique_vars_db[1]) + "= " + "'" + str(list_unique_vars_usr[0]) + "'"
                " AND " + variable2 + str(list_unique_vars_db[2]) + "=" + "'" + str(list_unique_vars_usr[1]) + "'"):

            if row[0] not in list_of_results:
                list_of_results.append(row[0])

    # Determine what to print for the user
    if (len(list_of_results) == 0):
        print("\nNo Results Found\n")
    else:
        print("\nResults")
        print("------------------------------------")
        for i in range(len(list_of_results)):
            print(str(i+1) + ". " + list_of_results[i])
        print("------------------------------------\n")


    # not sure what this is doing
    conn.commit()

    #Closing connections, online blurb said
    # sometimes if you don't close the connections it crates
    # problems
    c.close()
    conn.close()

  # Throws an error
  except:
        print("ERROR")
        print("------------------------------------")
        print("That is not an accepted command...")
        print("Type help and then press enter")
        print("To see a list of valid commands")
        print("Make sure you have run load data first")
        print("type load data, enter to create database")
        print("------------------------------------\n")



# Run the code
if __name__ == '__main__':
    main()

