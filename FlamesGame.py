flames = ["F", "L", "A", "M", "E", "S"]
string = "Relationship status"


def inputNames():
    global name1, name2
    name1 = input("Enter First Name: ")
    name2 = input("Enter Second Name: ")


def slashCommon():
    global name1List, name2List
    name1List = [*name1]
    name2List = [*name2]
    for letter in name1List:
        if letter in name2List:
            name1List.remove(letter)
            name2List.remove(letter)
    for letter in name2List:
        if letter in name1List:
            name1List.remove(letter)
            name2List.remove(letter)

def calculate():
    global total
    n1 = len(name1List)
    n2 = len(name2List)
    total = n1 + n2


def slashFlames():
    count = 1
    while len(flames) > 1:
        for cur in range(0, len(flames)):
            if count == total:
                flames.pop(cur)
                count = 1
            else:
                count += 1


def output():
    if flames[0] == "F":
        print(f"{string}: Friends")
    elif flames[0] == "L":
        print(f"{string}: Lovers")
    elif flames[0] == "A":
        print(f"{string}: Affectionate")
    elif flames[0] == "M":
        print(f"{string}: Marriage")
    elif flames[0] == "E":
        print(f"{string}: Enemies")
    elif flames[0] == "S":
        print(f"{string}: Siblings")


def game():
    inputNames()
    slashCommon()
    calculate()
    slashFlames()
    output()


game()
