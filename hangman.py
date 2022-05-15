import time
import random

print('\nWelcome to Hang-Man game\n')
time.sleep(2)
name = input('Enter your name: ')
time.sleep(2)
print('\nHello '+ name +' !Best of Luck!\n')

print('Game is about to start')
time.sleep(2)

def main():
    global word
    global dash
    global count
    global already_guessed
    global play_game
    global limit
    global length

    word_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                     "plants"]
    already_guessed = []
    word = random.choice(word_to_guess)
    length = len(word)
    dash = '_' * length
    limit = 5
    count = 0


def want_to_play():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

def hangman():
    global word
    global dash
    global count
    global already_guessed
    global play_game
    global limit
    global length

    guess= input('this is hangman word '+ dash +' guess a word: ')
    guess = guess.strip()
    if guess == 0 or guess <= '9' or len(guess) ==2:
        print('invalid input')
        hangman()
    elif guess in word:
        already_guessed.extend(guess)
        index=word.find(guess)
        word=word[:index]+'_'+word[index+1:]
        dash = dash[:index] + guess + dash[index+1:]
        print(dash+'\n')
    elif guess in already_guessed:
        print('Try another letter\n')
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess '+ str(limit-count) +' guess remaining\n')
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess '+ str(limit-count) +' guess remaining\n')
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess '+ str(limit-count) +' guess remaining\n')
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print('Wrong guess '+ str(limit-count) +' guess remaining\n')
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print('Wrong guess '+ str(limit-count) +' guess remaining\n')
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed, word)
            want_to_play()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        want_to_play()
    elif count != limit:
        hangman()
main()
hangman()