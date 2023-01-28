import random
import sys
attempt_list = []
attempts = 0
def show_score():
    if not attempt_list:
        print(f"you haven't played yet score is 0")
    else:
        print(f'your lowest number of attempts are {min(attempt_list)}')

def guess_des(number):
    
    if number < rand_number :
        return 'l'
    elif number > rand_number :
        return 'h'

    return 'c'



while True:
    wanna_play = input('Do u wanna play the game (Enter Yes/No): ')
    
    rand_number = random.randrange(1,11)
    
    while wanna_play.lower() == 'yes':
        attempts += 1        

        try:
            in_number = int(input('Pick a number between 1 and 10(Including): '))

            if in_number < 1 or in_number > 10:
                raise ValueError('Kindly enter the number between 1 to 10')


            de = guess_des(in_number) 

            if de == 'l':
                print('Number you guessed is lower than the actual number')
            elif de == 'h':
                print('Number you guessed is higer than the actual number')
            else:
                print('Hurray you guessed the number correctly')
                break
        except ValueError as err:
            print(f'{err}')
    attempt_list.append(attempts)
    while wanna_play.lower() == 'no':
        show_score()
        sys.exit('Ok buddy waiting for you')
    
    
    



