import random


class Game:
    def gen(self):
        options = ('rock', 'paper', 'scissor')
        num = random.randint(0, 2)
        op = options[num]
        return op

    def getInput(self):
        option = input("Enter your option: ")
        return option

    def start(self):
        genVal = str.lower(self.gen())
        genInVal = str.lower(self.getInput())
        print(f"Computer Chose   : {genVal}")
        if genVal == genInVal:
            print("Draw")
        elif genVal == 'rock' and genInVal == 'paper':
            print("You Win")
        elif genVal == 'rock' and genInVal == 'scissor':
            print("You Lose")
        elif genVal == 'paper' and genInVal == 'rock':
            print("You Lose")
        elif genVal == 'paper' and genInVal == 'scissor':
            print("You Win")
        elif genVal == 'scissor' and genInVal == 'paper':
            print("You Lose")
        elif genVal == 'scissor' and genInVal == 'rock':
            print("You Win")
        else:
            print("Invalid option")

    def repeat(self):
        val = input("Continue?(y/n): ")
        if val == 'y':
            return True
        elif val == 'n':
            return False
        else:
            print("Invalid Choice")
            exit(0)


game = Game()

while True:
    game.start()
    val = game.repeat()
    if val:
        pass
    elif not val:
        break

