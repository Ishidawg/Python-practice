# from termcolor import colored

print("==" * 18)
print("Signup system for two people")
print("==" * 18)

print("Before start... just type actual age!")
actualYear = int(input("What age we are? "))

# First person

name = input("Type your name: ")
bornYear = int(input("What year you born? "))
cpf = input("Type your cpf: ")

age = (actualYear - bornYear)

# Second person

print("==" * 18)
print("Next signup!")

name2 = input("Type your name: ")
bornYear2 = int(input("What year you born? "))
cpf2 = input("Type your cpf: ")

age2 = (actualYear - bornYear2)

# lists

firstPerson = [name, age, cpf]
secondPerson = [name2, age2, cpf2]

# result

print("==" * 18)
print("[1]Names - [2]CPF - [3]Age - [4]All?")
answer = int(input("What you want to show? "))

if answer == 1:
    print(firstPerson[0])
    print(secondPerson[0])
elif answer == 2:
    print(firstPerson[3])
    print(secondPerson[3])
elif answer == 3:
    print(firstPerson[2])
    print(secondPerson[2])

