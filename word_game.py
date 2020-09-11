import getpass

wrong = 0
right = 0

def pick_word():
    word = getpass.getpass("Choose the word: ")
    letters = list(word)
    return word, letters

def check_repetition(attempt, attempts_made):
    for letter in attempts_made:
        if letter == attempt:
            return 0
        
    return 1

def check_letter(attempt, hidden, word_letters):
    n_occ = 0
    pos = 0
    for letter in word_letters:
        if attempt == letter:
            n_occ+=1
            if chosen_word.find(letter) == 0:
                hidden = hidden.replace(hidden[chosen_word.find(letter)], letter,1)
                print(hidden)
            
            else:
                hidden_sub = hidden[0:pos]
                hidden_sub2 = hidden[pos:len(chosen_word)]
                hidden_sub2 = hidden_sub2.replace(hidden[pos], letter, 1)
                hidden = hidden_sub + hidden_sub2
        pos+=1

    if n_occ == 0:
        return 0, hidden
    
    else:
        return 1, hidden


chosen_word, word_letters = pick_word()
hidden = "*"*len(chosen_word)
print("Word: " + hidden)
attempts_made = []

while right < len(chosen_word):

    repetition = 0

    while repetition == 0:
        attempt = input("Pick a letter: ")
        repetition = check_repetition(attempt, attempts_made)

    attempts_made += attempt
    verification, hidden = check_letter(attempt, hidden, word_letters)    

    if verification == 1:
        right+=1
        print ("That letter is in the chosen word.")
    else:
        wrong+=1
        print ("That letter is not in the chosen word. You have a total of " + str(wrong) + " wrong guesses")

    print(str(verification) + '   ' + hidden)

    if wrong == 3:
        print("You lost the game. The word is " + chosen_word)
        break

    if hidden.find("*") == -1:
        print("Congratulations, you won the game.")

    print("==================================================")

