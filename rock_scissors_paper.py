# randomization

import random

random_integer = random.randint(0, 2)


#if random_integer == 1:
#    print("Head!")
#else:
#    print("Tails!")    

#print(random_integer)
 
#random_float = random.random() #random.uniform(1, 10)
#print(random_float)



#friends = ["lakshit", "luckie", "luck", "romeo", "juliet"]

#print(random.choice(friends))

#print (friends[random_integer])

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



game = [Rock, Scissor, Paper]

user = int(input("Enter 0,1,2 for Rock, Paper or Scissor: "))

if user>=3 or user<=0:
    print(f"You choose {user}")
    print (game[user])

computer = random.randint(0,2)
print(f"Computer choose: ")
print(game[computer])

if user>=3 or user<0:
    print("Invalid!")
if user == computer:
    print("Draw")
elif user==0 and computer==1:
    print("Computer wins")  
elif computer==0 and user==1:
    print("You win")            
elif user==1 and computer==2:
    print("Computer wins")  
elif computer==1 and user==2:
    print("You win")        
elif user == 2 and computer ==0:
    print("Computer wins")    
elif user==0 and computer==2:
    print("You win")      
    
    
