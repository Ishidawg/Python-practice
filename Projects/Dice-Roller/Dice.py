from termcolor import colored as c
import random as r

while True:
    print(c('DICE ROLLER GAME!', 'blue'))
    diceType = int(input(c('What is your dice? ', 'red')))
    diceValue = r.randint(1, diceType)
    print(c('Dice values is: ', 'blue'), c(f'{diceValue}', 'magenta'))
    ask = input(c('Roll again? yes or no? ', 'red'))
    if ask == 'no':
        break