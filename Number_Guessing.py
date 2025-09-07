import random

print("\n---Welcome to Number Guessing Game---\n   **Made By: ANKIT BUDHATHOKI**\n")
print("You Have 7 chances to guess the number. Let's Start!!\n")

low= int(input("Enter the Lower Bound:"))
high= int(input("Enter the Upper Bound:"))
print(f"\nYou Have 7 chance to guess the Number between {low} & {high}. Let's Start!!\n")

num=random.randint(low,high)
chance=7
count=0

while count < chance:
    count=count+1
    guess=int(input("Enter Your Guess:"))

    if guess==num:
        print(f"\nCongratulations!! You Guessed it correctly in {count}attempts")
        break
    elif count>=chance and guess!=num:
        print(f"\nThe Number was {num}. Better Luck Next Time!!")
    elif guess>num:
        print("Too high!!")
    elif guess<num:
        print("Too Low!!")

print("\n----Thanks For Playing---\n")
    
