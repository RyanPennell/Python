# this program was written in python2
import math
K = float(raw_input('Please input the value of K: '))
t = float(raw_input('Please input the time: '))
p = float(raw_input('Please input the price you paid: '))
P = float(raw_input('Please input the price of the security: '))
r = float(raw_input('Please input the rate as a decimal: '))
x= P-p
if P>K:
    print('The value of the return is approximately:')
    print(p-((P-K)*math.exp(-r*t)))
else :
    print('The value of the return is:')
    print(0)

