from gpiozero import Button

from gpiozero import LED

from time import sleep

from random import shuffle 

red = LED(19)

green = LED(4)

LeftButton = Button(17)
RightButton = Button(26)


lst = [red, green, red, red, green, green, red]
shuffle(lst)

for led in lst:
    led.on()
    sleep(.2)
    led.off()
    sleep(.1)

userSelection = []

while len(userSelection) < len(lst):
    if LeftButton.is_pressed:
        print("Green Pressed!")
        userSelection.append(green)
        LeftButton.wait_for_release()    
    elif RightButton.is_pressed:
        print("Red pressed!")
        userSelection.append(red)
        RightButton.wait_for_release()
    
hasWon = True        
for i in range(len(lst)):
    if lst[i] != userSelection[i]:
        hasWon = False
        break
if not hasWon:
    print("You lose!")
else:
    print("You win!")
    
    

