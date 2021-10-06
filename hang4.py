import  random
wins,lost=0,0
choices = ["guitar","advise", "unused", "hair", "library", "riddle", "unique", "fuel", "mountainous", "attach", "scared"]
flag=1
while flag:
    guesses = []
    max_errors = 7
    word=random.choice(choices)
    done = False
    print("*******************  HANGMAN  ********************")
    print("")
    print("1. To Play The Game")
    print("2.To end the game")
    print("")
    print("**************************************************")
    try:
        x=int(input("Enter your choice : "))
    except:
        x=3
    
    if(x==1):
        while not done:
            for letter in word:
                if letter.lower() in guesses:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("")
            print("")
            guess = input(f"Allowed Errors Left {max_errors}, Next Guess : ")
            guesses.append(guess.lower())
            if guess.lower() not in word.lower():
                max_errors -= 1
                if max_errors == 0:
                    break

            done = True
            for letter in word:
                if letter.lower() not in guesses:
                    done = False

        if done:
            print(f"You found the word! It was '{word}' ")
            wins=+1
        else:
            print(f"You lost. The word was '{word}'")
            lost+=1
    elif x==2:
        flag=0
        print("________________________________________________________")
        print("                     Game Over")
        print("Number of Wins : ",wins)
        print("Number of times lost : ",lost)
        print("________________________________________________________")
    else:
        print("Invalid Input. Choose 1/2")






