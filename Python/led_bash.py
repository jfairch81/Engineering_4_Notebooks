#!/bin/bash  #run program

echo "LED IN BASH" # lets u know program running


for i in {1..20} # Needs to turn on and off 10 times, 10 * 2 = 20
do
	/usr/bin/gpio -1 toggle 38 
	sleep 1  
done

