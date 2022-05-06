answer = 'n'

mylist = []

print("[Y] - [N]")

while answer != 'n' or answer != 'N':
    ask = input("Want to signup? ")

    if ask == 'y' or ask == 'Y':
        name = input("Type your name: ")
        age = int(input("Type your age: "))
        cpf = int(input("Type your CPF: "))
    else:
        break

    mylist.append(f"{name}, {age}, {cpf}")

for i in mylist:
    print(i)
