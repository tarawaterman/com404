class Bot:
    def __init__(self):
        self.name = """
        ~~~~~
        |BOT|
        ~~~~~"""
        self.age = """
        iiiiiiiiii
      |: : : : : :|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |: : :2:0:0:0: : :|
   |                 |
   ~~~~~~~~~~~~~~~~~~~"""
        self.energy = "|||||"
        self.shield = "⛨⛨⛨⛨⛨"
        self.summary =""


    def display(self):
        print("{} is {} years old and has {} energy and {} shield".format(self.name, self.age, self.energy, self.shield))

bot = Bot()
bot.display()