import pickle

while True:
    print("********************")
    print("*     Welcome      *")
    print("*   To Our Game!   *")
    print("********************")

    print("Type 'Start' to start!")
    print("Type 'Load' to load your save file!")

    if (input().lower() == "start"):
        print("started game")
        break

    elif (input().lower() == "load"):
        print("loaded save")
        break
    
    else: 
        print("Fucking type something right you twat")
