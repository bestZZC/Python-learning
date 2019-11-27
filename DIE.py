from random import randint
class Die:
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        self.sides=randint(1,6)
        return self.sides

new_die=Die()
count=0
while count<=10:
    print(new_die.roll_die())
    count=count+1