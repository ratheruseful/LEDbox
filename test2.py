import signal
from xbox360controller import Xbox360Controller
import board
import neopixel
import modes
import time

pixelCount = 520
pixels = neopixel.NeoPixel(board.D18,pixelCount, brightness=1, auto_write=False)
LEDArray = [(0,0,0)]*pixelCount

def stepArray():
    for i in range(pixelCount):
        pixels[i]=LEDArray[i]
    pixels.show()

    for i in range(pixelCount-1,0,-1):
        LEDArray[i]=LEDArray[i-1]

xbright=255

controller = Xbox360Controller(0, axis_threshold=0)
#foo = Xbox360Controller.get_available()

while (1):
    stepArray()
    r=g=b=0
    if controller.button_b.is_pressed:
        g=xbright
    if controller.button_a.is_pressed:
        g=int(xbright/2)
    if (controller.hat.y < 0):
        r=xbright
    if (controller.hat.x > 0):
        b=xbright
    if (controller.hat.y > 0):
        r=int(xbright/2)
    if (controller.hat.x < 0):
        b=int(xbright/2                     )
    LEDArray[0]=(r,g,b)
    time.sleep(0.05)

"""

def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))
    modes.white()


def on_button_released(button):
    print('Button {0} was released'.format(button.name))
    modes.black()


def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))
    modes.HSVfill((axis.x+1)/2,1,(axis.y+1)/2)


try:
    with Xbox360Controller(0, axis_threshold=0.2) as controller:
        # Button A events
        controller.button_x.when_pressed = on_button_pressed
        controller.button_x.when_released = on_button_released

        # Left and right axis move event
        controller.axis_l.when_moved = on_axis_moved
        controller.axis_r.when_moved = on_axis_moved

        signal.pause()
        

except KeyboardInterrupt:
    pass

"""