import string 
def encrypted(word, number):
 alphabet_upper = string.ascii_uppercase
 alphabet = string.ascii_lowercase
 encrypted_word = ""

 for letter in word:
     if letter in alphabet:
         index = alphabet.index(letter)
         new_index = (index + number) % 26
         encrypted_word += alphabet[new_index]
     elif letter in alphabet_upper :
         index = alphabet_upper.index(letter)
         new_index = (index + number) % 26
         encrypted_word += alphabet_upper[new_index]
     else:
         encrypted_word += letter

 print("Encrypted word:", encrypted_word)
def decrypted(word, number):
    alphabet_upper = string.ascii_uppercase
    alphabet = string.ascii_lowercase
    encrypted_word = ""
    if number == 3 :
     for letter in word:
         if letter in alphabet:
             index = alphabet.index(letter)
             new_index = (index - 3) % 26
             encrypted_word += alphabet[new_index]
         elif letter in alphabet_upper :
             index = alphabet_upper.index(letter)
             new_index = (index - 3) % 26
             encrypted_word += alphabet_upper[new_index]
         else:
             encrypted_word += letter

     print("Encrypted word:", encrypted_word)
    else :
        print("you can't decrypt this word, your entered number is wrong")
user_choice = input("Do you want to encrypt a word or decrypt a word? (encrypt/decrypt):").lower()
if user_choice == "encrypt":
    user_word = input("Enter a word: ")
    user_number = int(input("Enter a number: "))
    encrypted(user_word, user_number)
elif user_choice == "decrypt" :
     user_word = input("Enter a word: ")
     user_number = int(input("Enter a number: "))
     decrypted(user_word, user_number)
else :
    print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

