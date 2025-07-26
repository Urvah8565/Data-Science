import random

name = str(input("Enter your name : "))
print(f"Welcome to guess game : {name}  ")
rounds = 1
totalscore = 0
while True:
  scrtnum = random.randint(1, 10)
  score = 0

  attempts = 3 

  difficulty = (input("Enter difficulty level : (E)-Easy , (M)-Medium , (H)-Hard ")).lower()

  if difficulty == "e":
    print("Easy mode selected| You get 5 attempts")
    attempts = 5
  elif difficulty == "m":
    print("Medium level selected| You get 3 attempts")
    attempts = 3
  elif difficulty == "h":
    print("Hard level selected| You get 1 attempt ")
    attempts = 1 
  else:
    print("Invalid difficulty level selected, defaulting to 3 attempts")
    attempts = 3
  while attempts > 0:
    guess = int(input("Enter the number between 1 to 10 : "))
    
    if guess > scrtnum:
        print("Too high")
        attempts -= 1
        score-=2
    elif guess < scrtnum:
        print("Too low")
        attempts -= 1
        score-=2
    else:
        print("🚀🥳Correct number you win the game ")
        score+=1
        print(f"Score in round {rounds} is {score}")

        
        break
    
    if attempts > 0:
        print(f"Try again. {attempts} attempts left") 
    else :
     print ("You've used all attempts😥.game over")
     print(f"Score in round {rounds} is {score}")
     
  totalscore += score

  retry = input("Do you want to play again? (yes/no): ").lower()
  if retry != "yes":
     print(f"Thanks for playing! {name}")
     
     break
  else:
     print("Restarting the game...")
     rounds+=1



 
print(f"Total round played : {rounds} ")
print(f"final score with {rounds} rounds is : {totalscore}")
