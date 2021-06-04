import Adafruit_SSD1306
import Adafruit_LSM303
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

RST = 24
lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height 
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0) 

pad = 2
shape_width = 20
top = pad
bottom = height - pad
x = pad
fonts = ImageFont.load_default()

while True:
  
	acc, mag = lsm303.read() 
	acc_x, acc_y, acc_z = acc 
	mag_x, mag_y, mag_z = mag
	
	draw.text((x, top), "Accelerometer: ", font=font, fill=255) 
  
	draw.text((x, top + 10), "Acc x ={0}".format(round(acc_x / 100, 3)), font=font, fill=255) 
	draw.text((x, top + 20), "Acc y ={0}".format(round(acc_y / 100, 3)), font=font, fill=255) 
	draw.text((x, top + 30), "Acc z ={0}".format(round(acc_z / 100, 3)), font=font, fill=255) 

	disp.image(image) 
	disp.display()
	draw.rectangle((100, 12, 55, 50), outline=0, fill=0)
	disp.image(image)
	disp.display()
  
  
	time.sleep(.2)
