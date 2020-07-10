import board
import neopixel
import time

pixelCount = 520
pixels = neopixel.NeoPixel(board.D18,pixelCount, brightness=1, auto_write=False)
LEDArray = [(0,0,0)]*pixelCount
LEDArray[0]=(255,0,0)

for j in range(pixelCount):
    time1=time.time()
    for i in range(pixelCount):
        pixels[i]=LEDArray[i]       #write array
    time2=time.time()
    pixels.show()                   #show pixels
    time3=time.time()

    for i in range(pixelCount-1,0,-1):
        LEDArray[i]=LEDArray[i-1]   #step array
    time4=time.time()
    LEDArray[0]=(0,0,0)
    print('write array {0} show pixels {1} step array {2}'.format((time2 -time1)*1000,(time3 -time2)*1000,(time4 -time3)*1000))

    #time.sleep(0.01)