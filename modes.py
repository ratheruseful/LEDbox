import board
import neopixel
import time
import colorsys
import math
import random

pixelCount=150

pixels = neopixel.NeoPixel(board.D18,pixelCount, brightness=1, auto_write=False)

def smartSleep(startTime,delay):
 sleepTime=max(startTime+delay,time.time())-time.time()+0.0001
 time.sleep(sleepTime)
 return (time.time())

def white():
 pixels.fill((20,24,20))
 pixels.show()
	
def black():
 pixels.fill((0,0,0))
 pixels.show()

def RGBfill(r,g,b):
 pixels.fill((r,g,b))
 pixels.show()

def HSVfill(h,s,v):
 rgb = colorsys.hsv_to_rgb(h,s,v)

 pixels.fill((int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255)))
 pixels.show()

def s(s):
 time.sleep(s)

def colorTempFill(temperature,brightness):

 temperature /= 100
 
 if (temperature <= 66):
 
  red = 255
 
 else:
 
  red = temperature - 60
  red = 329.698727446 * pow(red,-0.133204)
  if (red < 0):
   red = 0
  if (red > 255):
   red = 255
 

 if (temperature <= 66):
 
  green = temperature
  green = 99.4708025861 * math.log(green) - 161.1195681661
  if (green < 0 ):
   green = 0
  if (green > 255):
   green = 255
 
 else:
 
  green = temperature - 60
  green = 288.1221695283 * pow(green,-0.0755148492)
  if (green < 0):
   green = 0
  if (green > 255):
   green = 255
 

 if (temperature >= 66):
 
  blue = 255
 
 elif (temperature <= 19):
  blue = 0
 
 else:
 
  blue = temperature - 10
  blue = 138.5177312231 * math.log(blue) - 305.0447927307
  if (blue < 0):
   blue = 0
  if (blue > 255):
   blue = 255
 
 pixels.fill((int(red*brightness),int(green*brightness),int(blue*brightness)))
 
def fire(mean,sd,frametime,brightness):

 temperature=mean
 mark=time.time()
 nextframe=mark+frametime
 
 while(1):
  colorTempFill(temperature,brightness)
  diff=temperature-mean
  temperature += random.randint(-sd-diff,sd-diff)
  waitTime = max(0,(nextframe-time.time()))
  if (waitTime==0):
   print("SLOW!")
  time.sleep(waitTime)
  nextframe=time.time()+frametime

def hueLoop(saturation,frametime,brightness):
 i=0
 mark=time.time()
 nextframe=mark+frametime
 
 while(1):
  HSVfill(i,saturation,brightness)
  waitTime = max(0,(nextframe-time.time()))
  if (waitTime==0):
   print("SLOW!")
  time.sleep(waitTime)
  nextframe=time.time()+frametime
  i += 0.01
  
def hueStrobe(saturation,frametime,brightness):
 i=0
 mark=time.time()
 nextframe=mark+frametime
 
 while(1):
  HSVfill(i,saturation,brightness)
  waitTime = max(0,(nextframe-time.time()))
  if (waitTime==0):
   print("SLOW!")
  time.sleep(waitTime)
  nextframe=time.time()+frametime
  black()
  waitTime = max(0,(nextframe-time.time()))
  if (waitTime==0):
   print("SLOW!")
  time.sleep(waitTime)
  nextframe=time.time()+frametime
  i += 0.01 
  
def hueBounce(saturation,frametime,brightness,hueStep,brightStep):
 i=0
 mark=time.time()
 nextframe=mark+frametime
 
 while(1):
  j=0
  while(j<brightness):
   HSVfill(i,saturation,j)
   waitTime = max(0,(nextframe-time.time()))
   if (waitTime==0):
    print("SLOW!")
   time.sleep(waitTime)
   nextframe=time.time()+frametime
   j+=brightStep
  while(j>0):
   HSVfill(i,saturation,j)
   waitTime = max(0,(nextframe-time.time()))
   if (waitTime==0):
    print("SLOW!")
   time.sleep(waitTime)
   nextframe=time.time()+frametime
   j-=brightStep
  i+=hueStep

def dither(brightness,dutyCycle,cycleTime):
  onTime = cycleTime*dutyCycle
  offTime = cycleTime-onTime
  startTime=time.time()

  while(1):
   HSVfill(0,1,brightness)
   startTime=smartSleep(startTime,onTime)
   black()
   startTime=smartSleep(startTime,offTime)

def rainbow(brightness,frametime,hueStep,hueStep2):
  hue = 0
  while(1):
    i=0
    innerHue=hue
    while (i<pixelCount):
      rgb = colorsys.hsv_to_rgb(innerHue,1,brightness)
      pixels[i]=((int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255)))
      i+=1
      innerHue+=hueStep
    pixels.show()
    hue+=hueStep2

def HSVbow(hueStep,hueStep2,satStep,satStep2,briStep,briStep2):
  hue = sat = bri = .999
  while(1):
    i=0
    innerHue=hue
    innerBri=bri
    innerSat=sat
    while (i<pixelCount):
      rgb = colorsys.hsv_to_rgb(innerHue,innerSat%1,innerBri%1)
      pixels[i]=((int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255)))
      i+=1
      innerHue+=hueStep
      innerBri+=briStep
      innerSat+=satStep
    pixels.show()
    hue+=hueStep2
    bri+=briStep2
    sat+=satStep2
      