#!/usr/bin/bash
#a script that takes in a url and displays it body size

curl "$1" | wc -c 
