#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 19:30:38 2021

@author: janmejoy
"""
from datetime import date
ref= date(2021, 5, 11)
today= date.today()
diff= today-ref
p= 29.53059
modulo= diff.days % p

def wxwn():
    if (modulo <= p/2):
        j= 'Waxing'
    else:
        j='Waning'
    return (j)

def phase(mod):
    ph= int(mod)
    if (ph== 15 ):
        i='Full Moon'
    elif (ph==0):
        i='New Moon'
    elif ((ph<15 and ph== 8) or (ph>15 and ph== 22)):
        i='Half Moon'
    elif (ph < 15):
        i='Crescent'
    else:
        i='Gibous'
    return(i)
        
print(today.strftime('%d/%m/%y'))
print ('Moon Age:',int(modulo), '/ 29.5 days')
print('Phase:', wxwn(), phase(modulo))
input ('Press ENTER to exit')
