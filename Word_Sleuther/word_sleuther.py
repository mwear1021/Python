import random
game = 'Word Sleuther'
word_bank = []
misplaced_letters = []
incorrect_letters = []
MAX_TURNS = 6
TURN = 0

#Open the .txt file with the list of words
with open('word_bank.txt', 'r') as word_file:
    #list comprehension to append all the words from the file to an empty list
    word_bank = [line.strip().lower() for line in word_file.readlines()]
    #choose a random word from the file
    winning_word = random.choice(word_bank)

print(f'Welcome to {game}.\nThe goal is to guess the 5-letter word in {MAX_TURNS} turns.\nYou will type your guess and then hit ENTER to submit your guess.')


#Main game loop
while TURN <= MAX_TURNS:
    
    user_guess = input('Your Guess: ').lower().strip()

    #Check for valid input
    if len(user_guess) != len(winning_word) or not user_guess.isalpha():
        print('Your guess must be 5 letters.')
    
    index = 0
    #iterate through each character in the guess and compare to the winning word
    for i in user_guess:
        if i == winning_word[index]:
            print(i.upper(), end='')
            if i in misplaced_letters:
                misplaced_letters.remove(i)
                

        elif i in winning_word:
            if i not in misplaced_letters:
                misplaced_letters.append(i)
            print('_',end='')
            

        else:
            if i not in incorrect_letters:
                incorrect_letters.append(i)
            print('_',end='')
        
        index += 1

    print('\n')
    print("Misplaced Letters: ", misplaced_letters)
    print("Incorrect Letters: ", incorrect_letters)
    TURN += 1

    if user_guess == winning_word:
        print("\nYou Win!")
        break

    if TURN == MAX_TURNS:
        print("\nSorry! You've used all your turns.")
        break

    print("You have", MAX_TURNS - TURN, "turns left.")