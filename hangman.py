import random

words = ["abra", "kaoe", "gusdhhu"]

guess = random.choice(words)
print(guess)

user = input("Guess a letter: ").lower()
for i in guess:
    if user == i:
        print("right")
    else:
        print("wrong")    
    
    
    
    
    #print(i)
    
    
    
    #if user == guess(user):
        #print("right")

