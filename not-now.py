# Makes a list of things you shouldn't search up right now.
import os

while True:
    # Asks what the user wants to do.
    user_decision = input("Do you want to read, append, or stop?: ")

    if user_decision == "read":
        not_now_file = open("/Users/ramteechua/Desktop/Files/project-not-now/not-now.txt", "r")
        contents = not_now_file.read()
        print("\n" + contents)
        not_now_file.close()
    elif user_decision == "append":
        words = input("What do you want to write?: ")
        not_now_file = open("/Users/ramteechua/Desktop/Files/project-not-now/not-now.txt", "a")
        not_now_file.write("• " + words + " \n")
        not_now_file.close()
    elif user_decision == "stop":
        break
    
    
    

