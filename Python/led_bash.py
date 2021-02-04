#!/bin/bash  #run program

echo "LED Running!" # easy for troubleshooting


for i in {1..20} # Needs to turn on and off 10 times, 10 * 2 = 20
do
	/usr/bin/gpio -1 toggle 38 
	sleep 1  # break in between so you can see it easily
done

