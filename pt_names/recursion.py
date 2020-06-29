#this is an attempt to solve the problem using recursion

from usingclassforimg import list_elements_info
from usingclassforimg import symbols_list
from usingclassforimg import initial_elements
import pdb

elements = list_elements_info(initial_elements())
symbols = symbols_list(elements)


def separate_name(name):	
#	pdb.set_trace()
	name_u = name.upper()	
	sep_name_u = list(name_u)
	return sep_name_u


def recursion(sep_name_u, sname):	
	i = len(sep_name_u)-1
	if i > -1:
		a = sep_name_u[i]  #m
		if i > 0:	
			b = sep_name_u[i-1] #g
			x = b + a #mg
			if x in symbols:
				sname.append(x)
				sep_name_u.pop()
				sep_name_u.pop()
				recursion(sep_name_u, sname)			
			elif a in symbols:
				sname.append(a)
				sep_name_u.pop()
				recursion(sep_name_u, sname)
			else:	
				sname.append('0')
		elif a in symbols:
			sname.append(a)
		else:
			sname.append('0')
	return(sname)	


print('Would you like to enter a name? (y/n)')
while input().lower() == 'y':
	print('Please enter a name.')
	symbol_name = []
	name = input()
	sname = recursion(separate_name(name), symbol_name)
	sname.reverse()
	if '0' in sname:
		print("Sorry, this name can't be printed with element symbols")
	else:
		print(sname)
	print('Would you like to enter another name?')
print('Ok, goodbye.')







