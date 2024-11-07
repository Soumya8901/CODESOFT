"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Coumputer choice(computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock 
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock wine 

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = scissor win 

C- Scissor 
Scissor - scissor = tie
Scossor - Rock = Rock win 
Scissor - Paper = scissor win

"""
import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print("User Choice = {User_choice}, computer Choice = {Comp_choice}")

if user_choice == comp_choice:
    print("Both choices same: Match Tie")
    
elif user_choice == "Rock":
     if comp_choice == "Paper":
         print("Paper covers Rock = Computer")
         
     else:
         print("Rock, Paper, Scissor = you win")
         
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, computer")
    else:
        print("Paper covers rocks, you win")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, you win")
    else:
        print("Rock smashes scissor, Computer win")       
             