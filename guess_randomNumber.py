# # random game 
# taking the users inputA
import random
guess=int(input("please enter your guess number : \t"))
random_num=random.randint(1,1000)
if guess==random_num:
    print("you won !")
else:
    print("loosed !!")
print(f"the guess no was {random_num}")
