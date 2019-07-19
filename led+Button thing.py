from gpiozero import Button

from gpiozero import LED

from time import sleep

red = LED(4)

green = LED(17)

LeftButton = Button(22)

RightButton = Button(27)

red.on()
sleep (.2)
red.off()
sleep (.2)
green.on()
sleep (.2)
green.off()
sleep (.2)
green.on()
sleep (.2)
green.off()
red.on()
sleep (.2)
red.off()

while True:
    if LeftButton.is_pressed:
    if RightButton.is_pressed:
    if RightButton.is_pressed:
    if LeftButton.is_pressed:
        green.on()
    else:
        red.on()

    
    
    
    
