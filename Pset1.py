#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 11:14:24 2019

@author: ry4n
"""

# user imports salary, amount they would like to save, and cost of their home
annual_salary = float(input("Please Enter your annaul salary: "))
save_perc = float(input("Please Enter the percent of salary to save, as a decimal: "))
total_cost = float(input("Please Enter the cost of your dream home:"))

#Setup of variables
down_payment = 0.25 * total_cost 
monthly_salary = annual_salary/12
current_savings = 0
r=0.04
portion_saved = save_perc * monthly_salary
t = 0

#Setup of algorithm

while current_savings < down_payment: 
        current_savings = current_savings*1.0033384306446
        current_savings += portion_saved 
        t += 1
        if current_savings > down_payment:            
            print("Number of months: ", t)
            
        

    






#Print answer to user
