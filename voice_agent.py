import os                                                   # importing os module to run system commands
if __name__ == '__main__' :
    print("Welcome to voice_agent 1.0 - created by piku")
    while True:                                             # keeps running until the user chooses to exit
        x = input("What do you want me to say: ")           # taking text input from the user
        if x == "p":                                        # exits the program if the user enters 'p'
            break
        command = f'espeak "{x}"'
        os.system(command)                                  # executes the command and speaks the text out loud