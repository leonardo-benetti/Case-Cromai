#!/bin/bash


while :
do
	# lê arquivo "pid"
	pid=$(<pid)
	
	# obtém os processos python ativos
	py_procs=$(pgrep python -d ' ')
		
	# verifica se os ID lido está nos processos ativos
	if [[ "$py_procs" == *"$pid"* ]]
	then
		echo "1: It is alive"
	else
		echo "1: It is dead"
		
		# executa o script python concorrentemente (&)
		python3 pythonscript.py &
	fi
	
	sleep 1
done
