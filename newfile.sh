#!/bin/bash
# Ask the user for their name
ROOT_DIR="/root/Python/"
echo "List of all files"
ls ${ROOT_DIR}
printf "\n\n"
echo Enter file name for creation or existing filename for other options?
read varname

system () {
  case "$options" in
      "d") rm -rf ${ROOT_DIR}$varname
         ;;
      "r") echo "Enter new filename"
         read newname
         mv ${ROOT_DIR}$varname ${ROOT_DIR}$newname ; chmod +x  ${ROOT_DIR}$varname
         ;;
       *) exit
         ;;
  esac  
} 

if test -f $varname 
then
   echo $varname already exists
   echo "Press 'd' for delete \n Press 'r' for rename \n Press '*' for exit"
   read options
   system
else
   cp ${ROOT_DIR}sample.py $varname ; chmod +x  ${ROOT_DIR}${varname}
   echo "File $varname created."
fi

