# CS205 Warm up (Team 8)
# January 27, 2020

# possibly needed module for later sql functionality
import sqlite3

def main():
    # initialize database & parser
    myinput = ""
    
    #creates bridge to database
    connection = sqlite3.connect("sample_database.db")

    #creates "point of command"
    pointer = connection.cursor()

    #
    while(myinput != "quit"):
        
        # gets user input
        myinput = raw_input("Waiting for user input: ")

        # checks if user asks for commands help
        if (myinput == "help"):
            help()
        if else (myinput == "quit"):
            #disconnects from database and ends program
            connection.close()
            break
        else:
            # listen for sql input
            command = "CREATE ... something ..., user input here"

            #execute sql statement
            pointer.execute(command)

            #saves changes to database
            connection.commit()



        

# displays list of commands
def help():
    print("help screen ... example command")

            
main()
