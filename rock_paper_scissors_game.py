import random

class RockPaperscissors():                                 # Main blueprint that manages the entire Rock Paper Scissors game
    def __init__(self):                                    # Initializing player and computer scores
        self.user_score = 0
        self.computer_score = 0    

    def play_round(self):                                  
        user_choice = self.user_choice()
        computer_choice = self.computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        self.winner(user_choice, computer_choice)

    def user_choice(self):                                 # Getting valid input from the user   
        while True:
            user_input = input("Choose one from rock, paper and scissors: ").strip().lower()
            if user_input in ("rock", "paper", "scissors"):
                return user_input
            else:
                print("Invalid input. Please choose rock, paper or scissors.")
        
    def computer_choice(self):                            # Getting random choice from the computer
        choices = ("rock","paper","scissors")
        return random.choice(choices)

    def winner(self, user, computer):                     # This method is used to add scores for user and computer on the basis of certain conditions.
        if user == computer:
            print("Draw")
        elif user == "rock" and computer == "scissors":
            print("User wins!")
            self.user_score += 1
        elif user == "scissors" and computer == "paper":
            print("User wins!")
            self.user_score += 1
        elif user == "paper" and computer == "rock":
            print("User wins!")
            self.user_score += 1
        else:
            print("Computer wins")
            self.computer_score += 1
        
    def play_again(self):                                  # Checiking whether the user wants to play more round or not.   
        while True:
            self.play_round()

            choice = input("Do you wanna play again? (y/n): ").strip().lower()

            if choice == "n":
                print("Thanks for playing!")
                break

    def score_compare(self):                              # Comparing scores of user and computer and returning the final winner on the basis of their total score
        if self.user_score > self.computer_score:
            print(f"You won the game :) \nYour score: {self.user_score}")
        elif self.computer_score > self.user_score:
            print(f"Computer won the game :( \n Computer's score: {self.computer_score}")
        else:
            print(f"Match Draw! Score: {self.user_score}-{self.computer_score}")

Game = RockPaperscissors()                                # Creating a Game object
Game.play_again()                                         # Controlling the whole game
Game.score_compare()                                      # Declairing the winner with it's total score


    



