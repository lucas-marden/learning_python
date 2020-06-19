#this is a password generator

#inputs: password length, types of inputs (lowercase, upper case, numbers, symbols)

pw_length = 25
c_lower = 'Y'
c_upper = 'Y'
c_numbers = 'Y'
c_symbols = 'Y'

import random

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = [x.upper() for x in lower]
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

pw = ''
list =[]

i = 1
while i < pw_length:
	if c_lower == 'Y':	
		a = random.choice(lower) 
		list.append(a)
	if c_upper == 'Y':
		b = random.choice(upper)
		list.append(b) 
	if c_numbers == 'Y':
		c = random.choice(numbers) 
		list.append(c)
	if c_symbols == 'Y':
		d = random.choice(symbols)
		list.append(d) 	
	ch = random.choice(list)
	pw += ch	
	i += 1

print(pw)


