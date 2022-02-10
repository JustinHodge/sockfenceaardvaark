#INCLUDES AND DECLARES
from pathlib import Path;
import random;
index_at_spec = 0
pw_security = 0
command = 'null'
#DEFINE FUNCTIONS
#this function is to generate a password
def CREATE_PWORD(pw_security):
    list_of_words = []#this chunk creates a list of words
    while (pw_security - 8 > 0 and pw_security > 8 and len(list_of_words) < 3):
        list_of_words.append(random.choice(long_words).rstrip())
        pw_security = pw_security - 1
    while (pw_security - 5 > 0 and pw_security > 5 and len(list_of_words) < 3):
        list_of_words.append(random.choice(medium_words).rstrip())
        pw_security = pw_security - 1
    while (len(list_of_words) < 3):
        list_of_words.append(random.choice(short_words).rstrip())
    #then we capitalize one word
    index_for_caps = list_of_words.index(random.choice(list_of_words))
    list_of_words.append(list_of_words[index_for_caps].upper())
    list_of_words.pop(index_for_caps)
    #then we shuffle them around
    random.shuffle(list_of_words)
    raw_password = "".join(list_of_words)
    #finally add a special charcter
    index_at_spec = random.randint(1, len(raw_password)  - 1)
    final_pass = raw_password[:index_at_spec] + random.choice(special_chars) + raw_password[index_at_spec:]
    print ("\n******************************************************************************\n")
    print ("         Your suggested password is :" + final_pass + "\n")
    print ("******************************************************************************\n\n\n")

#this is only to set how strong the password should be
def GET_PASSWORD_SECURITY():
    pw_security = -1
    while pw_security < 1 or pw_security > 10:
        try:
            print("\n----------------------------------------------------------------\n")
            pw_security = int(input("Choose a security level between 1 and 10 \n-----------------------------------------------------------------\n\n\n"))
        except:
            print("****Please use an integer between 1 and 10**** \n\n")
    return pw_security

#lets do this thing.
#make lists and stuff
list_of_words = []
long_words = open(Path('./long_words.txt')).readlines()
medium_words = open(Path('./medium_words.txt')).readlines()
short_words = open(Path('./short_words.txt')).readlines()
special_chars = ['!','@','#','$','%','^','&','*','(',')','<','>','?','{','}',':','.','/',';','[',']']

#finally call the functions
def Main():
    pw_security = -1
    command = "null"
    while command != "exit":
        print("\n-------------------------------------------------------------------------------\n")
        command = input("                   What would you like to do?\n--------------------------------------------------------------------------------\n\n\n")
        if command == "create":
            pw_security = GET_PASSWORD_SECURITY()
            CREATE_PWORD(pw_security)
        elif command == "repeat":
            if pw_security == -1:
                print ("\n There is no command to repeat. Please use create first\n")
            else:
                CREATE_PWORD(pw_security)
        elif command == "help":
                print("\nThe available commands are 'create' 'repeat' 'help' 'exit' \n")
        elif command == "exit":
            exit()
        else:
            print("\nNo valid command found. Try 'help'.")
            continue
def exit():
    print("\n---------------------------------------------------------------------------\n")
    print("Thanks for using Passgen. Goodbye!\n")
    print("---------------------------------------------------------------------------\n\n\n")
Main()
