answer = 'n'

mylist = []

print("[Y] - [N]")

while answer != 'N' or answer != 'n':
    result = input("Want to add names to list? ")

    if result == 'y' or result == 'Y':
        name = input("type a name: ")
    else:
        break

    mylist.append(f"{name}")

print(mylist)


