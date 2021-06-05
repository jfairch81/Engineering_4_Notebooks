import Adafruit_SSD1306
import Adafruit_LSM303
import math
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
lsm303 = Adafruit_LSM303.LSM303() 
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) 

disp.begin()
disp.clear()
disp.display()

height = disp.height 
width = disp.width
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image) 
draw.rectangle((0,0,width,height), outline=0, fill=0)

a = 2
shape_width = 20
top = a
bottom = height - a
x = a

font = ImageFont.load_default()
x_Change = 0

while True:

	x_Value = x_Change + x
  
	acc, mag = lsm303.read() 
	acc_x, acc_y, acc_z = acc 
	mag_x, mag_y, mag_z = mag 
  
	dataValue = abs(acc_x/10)
	if dataValue <= 3:
		dataValue = 3
		
	print(dataValue)

	draw.text((x, top), "Accelerometer: ", font=font, fill=255) 
	draw.text((x_Value, top + dataValue),".", font=font, fill=255) 	
	disp.image(image)
	disp.display()
	x_Change += 1

	time.sleep(.15)
