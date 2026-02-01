import random
word = random.choice(["apple", "banana", "cherry"])
display = ["_"] * len(word)
trying = 6
guessed_letters = []
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\n |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\n |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\n |
 / \n |
      |
=========''']

print("".join(display))
while "_" in display and trying > 0:
    gussed = input("Guess a letter: ")
    if gussed not in word:
      if gussed not in guessed_letters:
        trying -= 1
        print(hangman[6-trying])
        guessed_letters.append(gussed)
      elif gussed in guessed_letters :
        print("You already guessed that letter. Try again.")
        continue
    for i in range(len(word)) :
        if word[i] == gussed :
            display[i] = gussed 
            
    print("".join(display))
    print("You have", trying, "tries left")
if "_" not in display:
  print("You guessed the word: ", word,"\nand you still have",trying,"tries left")
elif trying == 0 :
    print("You lose! The word was: ", word)
    
