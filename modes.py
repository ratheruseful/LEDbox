import board
import neopixel
import time
import colorsys
import math
import random

pixels = neopixel.NeoPixel(board.D18, 30)

def white():
 pixels.fill((20,24,20))
	
def black():
 pixels.fill((0,0,0))

def RGBfill(r,g,b):
 pixels.fill((r,g,b))

def HSVfill(h,s,v):
 rgb = colorsys.hsv_to_rgb(h,s,v)

 pixels.fill((int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255)))

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

  