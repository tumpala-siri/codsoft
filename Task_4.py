import random

def game(current_user_score,current_computer_score) :
    print("              ***GET READY FOR ROCK PAPER SCISSORS!***")
    user_score=current_user_score
    computer_score=current_computer_score
    #user select the options
    user = input("choose a choice from rock , paper ,scissor :  ")
    options=["rock","paper","scissor"]

    #checking for user's input valid
    if user not in options:
        print("invalid options enter correct option")
        user = input("enter valid option: ")

    #computer select one choice from given options
    comp_choice = random.choice(options)

    # displaying computer choice
    print(" computer result : ",comp_choice)

    #game logic
    print(f"user choice is '{ user }' and computer choice is '{comp_choice}' ")
     
    if  (user == "rock" and comp_choice == "scissor") or  \
        (user == "scissor" and  comp_choice == "paper") or \
        (user == "paper" and comp_choice == "rock") :
           
        print("user is win")
        user_score += 1
            
    elif( user == comp_choice):
        print(" it's tie")
        print("    unfortunately no one is win  🙁  ")

    else:
        
        print("computer is win")
        computer_score += 1

    return user_score,computer_score

#starts exceution from here
# extracting user_score and computer score for multiple rounds
user_score,computer_score =  game(0,0)

print(f"user score : {user_score} And  computer score : {computer_score}")


def play_again(user_score,computer_score):
    play = input("Do you want to play again(say yes or no)!  ")

    if(play=="yes"):
        user_score,computer_score =  game(user_score,computer_score)
        print(f"user score : {user_score} And  computer score : {computer_score}")
        play_again(user_score,computer_score)

    else:
     print("        ****THANK YOU****")
     print("        I think you enjoyed lot 😊 ")

play_again(user_score,computer_score)
     
 