import time
print("Start guessing")

time.sleep(2)

word= input("Enter the word ?")
print('\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n''\n')
guesses = ''

turns=10

while turns >0:
    failed=0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1

    if failed==0:
        print("You won")
        break

    print()

    guess= input('Guess a character: ')

    guesses += guess

    if guess not in word:
        turns -=1
        print("wrong")

    print(f"You have {turns} turns left")
    print(f'The guesses you made : {guesses}')
if turns ==0:
    print("you lose")
    print(f'The entered word is {word}')
