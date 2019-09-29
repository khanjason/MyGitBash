#!/bin/bash
if [ -f "reminders.txt" ]; then	
	input="reminders.txt"
	while true; do
	while IFS=' ' read -r line
	do
  		#echo "line"
  		#echo "$line"
  		current=$(date +%d)
  		current+="/"
  		current+=$(date +%m)
  		current+="/"
  		current+=$(date +%Y)
  		current+=" "
  		current+=$(date +%H)
  		current+=":"
  		current+=$(date +%M)
  		current+=" "
                
		
  
  		lincut=${line%|*}
   
  		if  [ "$current" == "$lincut" ] ; 
then
 			
	       		echo "REMINDER"
        		echo "Reminder : ${line##*|}"
        		sleep 1m
			  
  		fi	
  
	done < "$input"
	done

fi
