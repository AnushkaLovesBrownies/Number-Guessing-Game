import random
print("number guessing game")
number=random.randint(1,9)
chance=0
print("guess a number between 1 and 9")
while chance < 5: 
     guess = int(input("Enter your guess:- "))
     if (guess==number):
      print("Congrats you won")
     elif (guess<number):
       print("oh you were really close")
     else :
       print("your guess was to high")
chance+=1
if not chance < 5: 
    print("YOU LOSE!!! The number is", number) 
 
