#!/usr/bin/env python3
import webbrowser as wb
print ("Piratebay adfree search \n")
x="https://pirateproxy.how/search.php?q="
z="&all=on&search=Pirate+Search&page=0&orderby="
a= input ("Enter Search Query (small letters): ")
l=a.split()
c="+"
y= c.join(l)
url= x+y+z
print (url)
wb.open(url, new=2)

