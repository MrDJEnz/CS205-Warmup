# CS205 Warm up (Team 8)
# January 27, 2020

# possibly needed module for later sql functionality
import sqlite3
import pandas

def main():
    # initialize database & parser
    myinput = ""
    
    #creates bridge to database
    connection = sqlite3.connect("top50.db")

    #creates "point of command"
    pointer = connection.cursor()

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
                connection.close()
                break
            else:
                # listen for sql input
                command = myinput
                #command = "SELECT TEMPORARY_COLOUMN"

                #execute sql statement
                pointer.execute(command)

                ##saves changes to database
                #connection.commit()
            print(myinput)
        except (RuntimeError):
            print("palceholder error")
        #except (sqlite3.OperationalError):
        #    print("SQL Syntax Error")


        

# displays list of commands
def help():
    print("help screen ... example command")
    print("FORMAT TO PARSE DATA AS FOLLOWS: ...")
    
            
main()
