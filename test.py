import modes
import time
import board
import neopixel
import xbox




#modes.dither(1,.01,5)

#pixels = neopixel.NeoPixel(board.D18, 400)

#modes.white()
#time.sleep(1)
"""
while(1):
    modes.RGBfill(0,0,0)
    time.sleep(1)
    modes.RGBfill(0,0,10)
    time.sleep(1)




on = (1,0,0)
off = (0,0,0)
bright = (10,0,0)

while (1):
 for i in range(30):   
  for j in range(i):
      start = time.time()
      pixels[j]=on
      pixels[j]=off
      print ((time.time() - start)*1000)






#

def testFunction(count):
    pixels[count-1]=(0,0,count)

for i in (1,4,10):
    pixels = neopixel.NeoPixel(board.D18, i)
    start = time.time()
    testFunction(i)
    print (str(i)+" pixels took "+str((time.time() - start)*1000))


modes.hueBounce(1,(60/1230),.2,0.71,.025)
def hueBounce2(saturation,frametime,brightness,hueStep,brightStep):
 i=0
 
 while(1):
  j=0
  while(j<brightness):
   modes.HSVfill(i,saturation,j)
   x=input()
   j+=brightStep
  while(j>0):
   modes.HSVfill(i,saturation,j)
   x=input()
   j-=brightStep
  i+=hueStep

#hueBounce2(1,(60/123),.5,0.71,.25)
"""
modes.black()
modes.rainbow(1,1,(1/300),(1/500))
#modes.HSVbow((1/300),.001,0,0,(1/50),0.001)
#modes.RGBfill(0,0,255)