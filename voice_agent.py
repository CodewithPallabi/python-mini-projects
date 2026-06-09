import os
if __name__ == '__main__' :
    print("Welcome to voice_agent 1.0 - created by piku")
    while True:
        x = input("What do you want me to say: ")
        if x == "p":
            break
        command = f'espeak "{x}"'
        os.system(command)