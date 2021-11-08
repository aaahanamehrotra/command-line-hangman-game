import re
import turtle
from fractions import *
from functions4game import *
pl_1 = input("Player 1 : ")
pl_2 = input("Player 2 : ")
print(pl_1 )
word = input( "enter a word : ").upper()
word_letters = list(word)
c = len(word_letters)
guessed = list()
for letter in range(len(word_letters)):
    guessed.append("_ ")
print(guessed)
i = Fraction(1, c)
correct_guesses = list()
g = 6
while g > 0:
    print(pl_2 )
    guess = input( "guess a letter: ").upper()
    for a in word:
        if a == guess:
            b = [i.start() for i in re.finditer(a, word)]
            for c in b:
                guessed.pop(c)
                guessed.insert(c , guess)
            m = list()
            for l in b:
                k = l + 1
                m.append(k)
            f = (f'That\'s a great guess. Keep going!! ')
            correct_guesses.append(guess)
            check =  all(item in correct_guesses for item in word_letters)
            if check is True:
                print(guessed)
                print(f'{pl_2} wins . Congrats {pl_2}.\n {pl_1}, keep trying. Better luck next time. The correct word was {word} ')
                exit()
            elif check is False:
                continue
        elif guess not in word:
            if g == 6:
                make_head()
                f = (f'oh! That\'s not a good guess .It\'s alright. You can try again. You still have {g} guesses remaining.  ')
            elif g == 5:
                make_body()
                f = (f'oh! That\'s not a good guess .It\'s alright. You can try again. You still have {g} guesses remaining.  ')
            elif g == 4:
                make_rhand()
                f = (f'oh! That\'s not a good guess .It\'s alright. You can try again. You still have {g} guesses remaining.  ')
            elif g == 3:
                make_lhand()
                f = (f'oh! That\'s not a good guess .It\'s alright. You can try again. You still have {g} guesses remaining.  ')
            elif g == 2:
                make_rleg()
                f = (f'oh! That\'s not a good guess .It\'s alright. You can try again. You still have {g} guesses remaining.  ')
            elif g == 1:
                make_lleg()
                f = (f'oh! That\'s not a good guess .It\'s alright. You can try again. You still have {g} guesses remaining.  ')
            g -= i
    print(guessed)
    print(f)
    print(f'You have {g} guesses remaining')
    if g > 0:
        b = (f'oh! That\'s not a good guess .It\'s alright. You can try again. You still have {g} guesses remaining.  ')
    elif g <=0:
        b = (f'{pl_1} wins . Congrats {pl_1}.\n {pl_2}, keep trying. Better luck next time. The correct word was {word} ')

print(b)
