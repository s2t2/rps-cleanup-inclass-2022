



from random import choice


# why remove duplication?
# so in the future we only need to update the code in one place
# so we aren't able to forget to update all the places
valid_choices = ["rock", "paper", "scissors"]


def winner(user_choice, computer_choice):
    if user_choice == "rock" and computer_choice == "rock":
        #print("It's a tie!")
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "paper":
        #print("The computer wins")
        return "The computer wins"
    elif user_choice == "rock" and computer_choice == "scissors":
        #print("The user wins")
        return "The user wins"

    elif user_choice == "paper" and computer_choice == "rock":
        #print("The computer wins")
        #return "The computer wins" # BUG!! OOPS :-)
        return "The user wins"
    elif user_choice == "paper" and computer_choice == "paper":
        #print("It's a tie!")
        return "It's a tie!"
    elif user_choice == "paper" and computer_choice == "scissors":
        #print("The user wins")
        #return "The user wins" # BUG!! OOPS :-)
        return "The computer wins"

    elif user_choice == "scissors" and computer_choice == "rock":
        #print("The computer wins")
        return "The computer wins"
    elif user_choice == "scissors" and computer_choice == "paper":
        #print("The user wins")
        return "The user wins"
    elif user_choice == "scissors" and computer_choice == "scissors":
        #print("It's a tie!")
        return "It's a tie!"



if __name__ == "__main__":

    # ONLY RUN THE FOLLOWING CODE IF WE RUN THIS SCRIPT FROM THE COMMAND LINE
    # BUT NOT IF WE ARE IMPORTING SOME CODE FROM THIS FILE TO ANOTHER FILE
    # PREVENTS EXECUTION OF THE CODE BELOW WHEN ALL WE WANT TO DO IS IMPORT / TEST A FUNCTION IN ISOLATION


    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_choices:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_choices)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    if u == "rock" and c == "rock":
        print("It's a tie!")
    elif u == "rock" and c == "paper":
        print("The computer wins")
    elif u == "rock" and c == "scissors":
        print("The user wins")

    elif u == "paper" and c == "rock":
        print("The computer wins")
    elif u == "paper" and c == "paper":
        print("It's a tie!")
    elif u == "paper" and c == "scissors":
        print("The user wins")

    elif u == "scissors" and c == "rock":
        print("The computer wins")
    elif u == "scissors" and c == "paper":
        print("The user wins")
    elif u == "scissors" and c == "scissors":
        print("It's a tie!")
