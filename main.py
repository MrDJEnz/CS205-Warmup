# CS205 Warm up (Team 8)
# January 27, 2020
    
def main():
    # initialize database & parser
    myinput = ""

    while(myinput != "quit"):
        myinput = raw_input("Waiting for user input: ")
        # listen for sql input

        if (myinput == "help"):
            help()
        

def help():
    print("help screen")

def initSQL():
    print("SQL functionality")
            
main()
