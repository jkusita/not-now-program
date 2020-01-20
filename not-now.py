# Makes a list of things you shouldn't search up right now.
import os
folder_path = ""
while True:
    # Asks what the user wants to do.
    user_decision = input("Do you want to read, append, or stop?: ")

    if user_decision == "read":
        not_now_file = open(folder_path, "r")
        contents = not_now_file.read()
        print("\n" + contents)
        not_now_file.close()
    elif user_decision == "append":
        words = input("What do you want to write?: ")
        not_now_file = open(folder_path, "a")
        not_now_file.write("• " + words + " \n")
        not_now_file.close()
    elif user_decision == "stop":
        break
    
    
    

