#!/bin/bash  #allows you to run the program by just typing its name

echo "LED BLINK IN BASH" #pints that the program is running


for i in {1..20} #to turn on an off 10 times, you need to change it 20 times
do
	/usr/bin/gpio -1 toggle 38   #selects the physical pin number, and toggles
	sleep 1  #little sleep to not have the LED go crazy
done

