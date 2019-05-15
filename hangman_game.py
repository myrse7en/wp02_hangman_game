# Imports general words to the word bank
from random import choice

# Importing for clearing capabilities
from IPython.display import clear_output

import sys
import os
cls = lambda: os.system('cls')

def gameDiff(diff):
    if diff.lower() == 'x':
        return 1
    elif diff.lower() == 'h':
        return 3
    elif diff.lower() == 'm':
        return 5
    else:
        return 7


def gameDisplay():
    print('  ' + secret_sol.upper())
    print('\nGuesses remanining: {}'.format(guesses))
    print('You have tried: {}'.format(sorted(prev_ans)))


def solDisplay(secret, cur_space, rec_guess):
    # print(secret, cur_space, rec_guess) test line
    result = ""

    for i in range(len(secret)):
        if secret[i] == rec_guess:
            result = result + rec_guess
        else:
            result = result + cur_space[i]
    return result


#ask
# def gameCore():
#         if len(ans) != 1:
#             print('You entered more than one character. Try again.')
#         elif ans in sol:
#             print('Nice!! {} is in the word!'.format(ans))
#             secret_sol = solDisplay(sol, secret_sol, ans)
#         elif ans in secret_sol:
#             print('You have already guessed that. Try again.')
#         else:
#             guesses -= 1
#             print('Wrong!! {} is not in the word!'.format(ans))


def graphicHangmanBasic(guesses):
    """ Draws basic hangman animation based on guess count """
    print("")
    if guesses == 10:
        print("+======+      ")
        print("|  *   *   *  ")
        print("|    *   *    ")
        print("|     \\0/    ") #prints incorrectly without double backslash
        print("|      |      ")
        print("|     / \     ")
        print("|_____________")
        print("")
        print("You LIVED to play another day...")
    elif guesses == 7:
        print("+======+      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|_____________")
        print("")
    elif guesses == 6:
        print("+======+      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|_____________")
        print("")
    elif guesses == 5:
        print("+======+      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|_____________")
        print("")
    elif guesses == 4:
        print("+======+      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
        print("|_____________")
        print("")
    elif guesses == 3:
        print("+======+      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
        print("|_____________")
        print("")
    elif guesses == 2:
        print("+======+      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
        print("|_____________")
        print("")
    elif guesses == 1:
        print("+======+      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
        print("|_____________")
        print("")
    elif guesses == 0:
        print("+======+      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("|_____________")
        print("")
        print("The noose tightens around your neck...")


words_general_l = ['account', 'addition', 'adjustment', 'advertisement', 'agreement', 'amount', 'amusement', 'animal', 'answer', 'apparatus', 'approval', 'argument', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'balance', 'behavior', 'belief', 'breath', 'brother', 'building', 'business', 'butter', 'canvas', 'chance', 'change', 'comfort', 'committee', 'company', 'comparison', 'competition', 'condition', 'connection', 'control', 'copper', 'cotton', 'country', 'credit', 'current', 'damage', 'danger', 'daughter', 'decision', 'degree', 'design', 'desire', 'destruction', 'detail', 'development', 'digestion', 'direction', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 'distribution', 'division', 'driving', 'education', 'effect', 'example', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'family', 'father', 'feeling', 'fiction', 'flight', 'flower', 'friend', 'government', 'growth', 'harbor', 'harmony', 'hearing', 'history', 'impulse', 'increase', 'industry', 'insect', 'instrument', 'insurance', 'interest', 'invention', 'journey', 'knowledge', 'language', 'learning', 'leather', 'letter', 'liquid', 'machine', 'manager', 'market', 'measure', 'meeting', 'memory', 'middle', 'minute', 'morning', 'mother', 'motion', 'mountain', 'nation', 'number', 'observation', 'operation', 'opinion', 'organisation', 'ornament', 'payment', 'person', 'pleasure', 'poison', 'polish', 'porter', 'position', 'powder', 'process', 'produce', 'profit', 'property', 'protest', 'punishment', 'purpose', 'quality', 'question', 'reaction', 'reading', 'reason', 'record', 'regret', 'relation', 'religion', 'representative', 'request', 'respect', 'reward', 'rhythm', 'science', 'secretary', 'selection', 'servant', 'silver', 'sister', 'sneeze', 'society', 'statement', 'stitch', 'stretch', 'structure', 'substance', 'suggestion', 'summer', 'support', 'surprise', 'system', 'teaching', 'tendency', 'theory', 'thought', 'thunder', 'transport', 'trouble', 'vessel', 'weather', 'weight', 'winter', 'writing']


# main program begins
flag = True
# game loop begins
while flag == True:
    clear_output(); cls()
    graphicHangmanBasic(7)

    sol = choice(words_general_l)
    prev_ans = []

    diff = input("Select Wanted Level:\n\t(E) -- Outlaw\n\t(M) -- Cattle Hustler\n\t(H) -- Bank Robber\n\t(X) -- Courting Death\n\t ")
    clear_output(); cls()

    guesses = gameDiff(diff)

    secret_sol = '-' * len(sol)

    # print game progress
    graphicHangmanBasic(guesses)
    gameDisplay()

    # check guess loop begins
    while guesses > 0 and not sol == secret_sol:

        # ask the user what they would like to do
        ans = input('\nGuess one letter (quit to escape): ')
        ans = ans.lower()

        # clear output from previously displayed grid
        clear_output(); cls()

        # base case, break on quit
        if ans == 'quit':
            graphicHangmanBasic(guesses)
            print('You escaped the noose!')
            print("The word was: {}".format(sol.title()))
            print('\nThanks for playing!\n\t\t\tauthor:myrse7en')
            break
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<possible easter egg here
        elif ans == '111191':
            clear_output(); cls()
            print("\n\n\t /^^\   /^^\\\n\t(    \_/    ) \n\t \    M    /\n\t  \   A   /\n\t   \  R  /\n\t    \ I /\n\tFOR  \A/ ONE\n\t  MY  ^   AND\n    **  **  TRULY  **  **")
            sys.exit()
        else:
            clear_output(); cls()
            graphicHangmanBasic(guesses)
            gameDisplay()
            if len(ans) != 1:
                print('\nYou did not enter your guess correctly. Try again.')
            else:
                secret_sol = solDisplay(sol, secret_sol, ans)
                if ans in prev_ans:
                    print('\nYou have already guessed that. Try again.')
                elif ans in sol:
                    clear_output(); cls()
                    prev_ans.append(ans)
                    graphicHangmanBasic(guesses)
                    gameDisplay()
                    print("\n{}!! '{}' is in the word!".format(choice(['Awesome', 'Sweet', 'Great', 'Excellent']), ans))
                elif ans not in sol:
                    guesses -= 1
                    clear_output(); cls()
                    prev_ans.append(ans)
                    graphicHangmanBasic(guesses)
                    gameDisplay()
                    print("\nWrong!! '{}' is not in the word!".format(ans))
    if guesses <= 0:
        clear_output(); cls()
        graphicHangmanBasic(0)
        print("...GAME OVER!...")
        print("\nThe word was: {}".format(sol.title()))
    elif guesses >= 0 and ans != 'quit':
        clear_output(); cls()
        graphicHangmanBasic(10)
        print("...YOU WIN!...")
        print("\nThe word was: {}".format(sol.title()))
    # main loop ends
    ans = input('\nGive it another hang? (Y/N): ')
    if ans.lower() == 'n':
        clear_output(); cls()
        print('\n\n\tEvery day above ground is a good day!\n\n\n\n\n')
        flag = False
    # <<<<<<<<<<<<<<<<<<<<<<<<possible easter egg here

# main program ends
