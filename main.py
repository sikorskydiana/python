import random

from hangman import hangmanpics
from hangman_words import words
from hangman import logo

#words = ["camels", "elephant", "tiger", "lion", "giraffe", "monkey"]
word = random.choice(words)
print("Welcome to Hangman Game!")
print(f"Pssst, the solution is: {word}")

display = []
for n in range(len(word)):
  display += "_"
#print(display)
#print(f"{' '.join(display)}")
i = 0
lives = 6
end_of_the_game = False

while lives != 0 and not end_of_the_game:
 
  while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    #guess = "f"
    
    
    if guess in word:
      print("Right")
      for posizione in range(len(word)): 
        letter = word[posizione]
        if letter == guess:
          display[posizione] = letter
          print(f"{' '.join(display)}")
          #print(display)
          print(hangmanpics[lives])
         
          
     # posizione = word.index(guess)
     # display[posizione] = guess
    #  print(display)
      #i += 1
    
    if "_" not in display:
      end_of_the_game = True
      print(f"You win! The word is {word}")
      print(logo)
      
       
    elif guess not in word:
      print("Wrong! You lost one life")
      lives -= 1
      print(hangmanpics[lives])
      print(f"Оnly {lives} left")
     
      if lives==0:
        end_of_the_game= True
        print("You lost all of your lives. YOU LOSE!")


    



  

