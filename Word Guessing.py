secretWord = "Ankush"                 #Secret word the player needs to guess
Guessed = ""

failure_count = 3                       # No. of chances for one player

while failure_count > 0:
    guess = input("Enter a letter: ").lower()
    
    if guess in secretWord:
        print(f"Correct! There is one or more {guess} in the secret word")
        
    else:
        failure_count -= 1 
        print(f"Incorrect! There are no {guess} in the secret word. {failure_count} chances left.")
        
letters_Guessed = Guessed + guess
wrong_letter_count = 0 

for letter in secretWord:
    if letter in letters_Guessed:
        print(f"{letter}" , end= "")
        
    else:
        print(".....", end = "")
        wrong_letter_count += 1
        
if wrong_letter_count == 0:
    print(f"Congratulations! You have won and the word was: {secretWord}")

else:
    print("Sorry! You lose!")

        

    