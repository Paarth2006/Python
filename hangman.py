import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

display = []

for i in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Enter a Letter:").lower()

    if guess in display:
        print("You have already guessed",guess)

    for j in range(word_length):
        letter = chosen_word[j]
        #print("Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[j] = letter

    if guess not in chosen_word:
        print(f"You Guessed {guess},thats not the word.")
        lives -= 1
        print((lives),"lives left")
        if lives == 0:
            end_of_game=True
            print("You Lose\nGame Over")

    print(''.join(display))

    if "_" not in display:
        end_of_game = True
        print("Yes!! That's the Word\nYou Win")
    from hangman_art import stages
    print(stages[lives])