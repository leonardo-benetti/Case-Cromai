#!/bin/bash


while :
do
	pid=$(<pid)
		
	if kill -0 "$pid"  > /dev/null 2>&1;
	then
		echo "1: It is alive"
	else
		echo "1: It is dead"
		python3 pythonscript.py &
	fi
	
	sleep 1
done
