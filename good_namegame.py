def play_game():
    print("Do you want to play a game? (yes/no)")
    user_input = input().lower()

    if user_input == "yes":
        print("Great! Let's play.")

        print("What is your name?")
        name = input()

        if name.lower() == "tom":
            print("You suck.")
        
        
        elif name.lower() == "zac":
            print("You are a bitch.")
        
        
        else:
            print("Nice to meet you, " + name + "!")
            print("Have a great day!")
    else:
        print("Lame!")

    # Call the play_game function recursively
    play_game()


# Call the play_game function for the first time
play_game()

