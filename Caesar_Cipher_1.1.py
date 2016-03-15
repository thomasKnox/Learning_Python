"""
 Caesar_Cipher_1.1.py
 Encrypts/Decrypts phrases based on specified shift
 Author: Thomas Knox <March, 2016>
"""

# used for shifting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# displays the new phrase
def display_new_phrase(phrase, encrypted):
    if encrypted == True:
        print "Encrypted phrase: %s\n" % phrase
    else:
        print "Decrypted phrase: %s\n" % phrase

# encrypts the phrase
def encrypt_letters(phrase, shift):
    encrypted_phrase = ""
    # for each letter in the phrase
    for letter in phrase.lower():
        if letter.isalpha():
            # if a space
            if letter == ' ':
                encrypted_phrase += " "
            # if the index is greater than the shift from 'z'
            elif (alphabet[alphabet.index(letter)] > (26 - int(shift))):
                # add the letter from the differance starting at 'a' 
                encrypted_phrase += alphabet[(alphabet.index(letter) + int(shift)) - 26]
            else:
                encrypted_phrase += alphabet[alphabet.index(letter) + int(shift)]
        else:
            encrypted_phrase += letter
    # pass encrypted phrase to be displayed
    display_new_phrase(encrypted_phrase, True)

# decrypts the phrase
def decrypt_letters(phrase, shift):
    decrypted_phrase = ""
    # for each letter in the phrase
    for letter in phrase.lower():
        if letter.isalpha():
            # if a space
            if letter == ' ':
                decrypted_phrase += " "
            # if the index is less than the shift from zero - 'a'
            elif (alphabet[alphabet.index(letter)] < (0 + int(shift))):
                # add the letter from the differance starting at 'a' 
                decrypted_phrase += alphabet[0 + (alphabet.index(letter) - int(shift))]
            else:
                decrypted_phrase += alphabet[alphabet.index(letter) - int(shift)]
        else:
            decrypted_phrase += letter
    # pass decrypted phrase to be displayed
    display_new_phrase(decrypted_phrase, False)

# gets the phrase from the user
def setup_cipher():
    choices = ["Encrypt", "Decrypt", "Exit"]
    
    choice = raw_input("[0] " + choices[0] + "\n" +
                       "[1] " + choices[1] + "\n" +
                       "[2] " + choices[2] + "\n" +
                       "What would you like to do: ")
    # if a valid choice
    if choice.isdigit() and int(choice) < 3:
        # exit
        if int(choice) == 2:
            raw_input("Press Enter to exit...")
            exit()
        else:
            # get phrase data
            shift = raw_input("Enter alphabetic shift: ")
            phrase = raw_input("Enter the phrase to %s: " % choices[int(choice)])
            
            # encryption
            if int(choice) == 0:
                encrypt_letters(phrase, shift)
            # decryption
            elif int(choice) == 1:
                decrypt_letters(phrase, shift)
    # error
    else:
        print "Error - Choice Invalid\n"
        setup_cipher()
        
# MAIN
while True:
    setup_cipher()
