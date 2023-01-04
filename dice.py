import random
class Dice:
    def roll(self):
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        #print(number1)
        #print(number2)
        dice_num = (number1, number2)
        return dice_num


dice_val = Dice()
dice_tup = dice_val.roll()
print(dice_tup)
#dice_tup.append(5)
#print(f"dice_tup after append: {dice_tup}")

