#!bin/bash

if [ $(ps -ef | grep -c "ssh") -gt 1 ]; 
then
       	echo "true"; 
fi
