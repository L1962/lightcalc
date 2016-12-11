# Written as a quick power consumption calculator for CLI linux.

import math
import os

#This clears the screen:
os.system('clear');

#Gather inputs:
watts = int(input("How many watts does your bulb use? "));
bulbs = int(input("\nHow man bulbs are you going to use? "));
time = float(input("\nHow many hours per day are you running the lights? "));
watthour = float(input("\nHow much is your kilowatt hour? "));

#Calculations:
usehour = int(watts*bulbs);
day = int(watts*bulbs*time);
cost = float(watts*bulbs*time*watthour);
kwh = float(cost/1000);
month = float(kwh*30);
cycle = float(kwh*63);

#Conversions to use in the output:
usehour = str(usehour);
day = str(day);
kwh = str(kwh);
month = str(month);
cycle = str(cycle);

#Final outputs:
print("\nYour lights will use " + usehour + " watts an hour.\n");
print("It will use " + day + " watts in a grow cycle DAY.\n");
print("It will cost $" + kwh + " per day to run\n");
print("You will spend $" + month + " in a 30 day month.\n");
print("It will cost $" + cycle + " for an entire flower cycle of 9 weeks.\n");

#Written by Leopold Smith L1962 on github