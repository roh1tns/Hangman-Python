import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

word_length = len(chosen_word)
display = ['_']*len(chosen_word)

end_of_game = False

lives = 6
guessed_list = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess in guessed_list:
        print(f'You have already guessed the letter {guess}\n____________________________________________________')
        continue

    guessed_list.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print(f'{guess} is not in the word! You lost a life')
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(hangman_art.stages[lives])
    for i in display:
        print(i, end='')
    print()
    if '_' not in display:
        end_of_game = True
        print("You Win!")

    print('____________________________________________________')
