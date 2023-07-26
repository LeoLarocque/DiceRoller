import random
#Dice roller.
def function():
    while 1 == 1:
        q = input('This is a dice roller if you would like to continue type "yes". ')
        if q == "yes":
            print(str(random.randint(1, 6)))
        else:
            print("Goodbye!")
            break
function()
