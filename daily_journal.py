from datetime import datetime                                          # Importing Datetime module to track date in journals
import os

def new_entry():                                                       # Creating a function that automatically add new journals into the JOURNALS folder
    if not os.path.exists("journals"):
        os.mkdir("journals")
    
    now = datetime.now()                                               # Returning current time 
    today = now.date()                                                 # Returning today's date
    filename = os.path.join("journals",f"journal_{today}.md")          # Creating an list element in JOURNALS folder which is the name of the journal

    while True:                                                        # Creating an infinite loop that runs continuously until the user wants to stop journaling
        title = input("Enter title: ")
        entry = input("Write your journal: ")
        current_time = datetime.now().strftime("%I:%M %p")             # Getting the current time and formatting it for journal entries

        with open(filename, "a") as file:                              # Opening the journal file in append mode to add new journal entries
            file.write(f"# {title}\n")                                 # Writting the title as heading      
            file.write(f"Date: {today}\n")                             # Adding the date
            file.write(f"Time: {current_time}\n")                      # Adding time
            file.write(f"{entry}\n")                                   # Saving data given by the user in journal
        
        choice = input("Add another entry? (y/n): ").lower().strip()   # Asking the user if they wanna add another entry or not
        if choice == "n":                       
            break                                                      # Breaking the loop

def view_journals():                                                   # This function is used for creating an internal list of all existing journals
    files = os.listdir("journals")

    print("-------Existing Journals-------\n")
    for idx, file in enumerate(files, start=1):                        # Iterating over the files list and giving each journals with an index number
        print(f"{idx}.{file}")
    
new_entry()                                                            # calling the functions
view_journals()