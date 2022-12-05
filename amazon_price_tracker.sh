#!/bin/bash
#insert url to check price. Prices will be logged to a file on Desktop.
#Notification of the price will appear when the script is run.

url="https://www.amazon.in/Casio-G-Shock-Analog-Digital-Black-Watch-GA-B001-1ADR/dp/B0BGNR9HBG/ref=sr_1_11?keywords=gshock+watch+for+men&qid=1670278341&sprefix=gsho%2Caps%2C394&sr=8-11"

mkdir -p ~/Desktop/folder
cd ~/Desktop/folder
wget "$url"
price=$(cat * | grep -i pricetopay | cut -d ">" -f 6 | cut -d "<" -f 1)
name=$(echo $url | cut -d "/" -f 4)
notify-send $name $price
rm -r ~/Desktop/folder
echo $price>>~/Desktop/$name"_log.txt"

