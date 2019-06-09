#this program is written in python2
rate = float(raw_input('Please input your rate like 0.06 for 6 percent: '))
time = float(raw_input('Please enter the number of months: '))
value = float(raw_input('Please enter the ending value with no $ sign nor commas: '))
n = 0
sum = 0
while n < time+1:
    sum = sum+ (1+ rate/12)**n
    n += 1

princ = value/sum
print "Your pricipal must be:"
print  princ
