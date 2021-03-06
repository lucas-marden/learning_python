#this is an attempt to solve the problem using recursion

from usingclassforimg import list_elements_info
from usingclassforimg import symbols_list
from usingclassforimg import initial_elements
import pdb
from usingclassforimg import initial_elements
from combination import display_image
from PIL import Image

elements = list_elements_info(initial_elements())
symbols = symbols_list(elements)


def separate_name(name):	
#	pdb.set_trace()
	name_u = name.upper()	
	sep_name_u = list(name_u)
	return sep_name_u


def write_symbol_name(sep_name_u, sname):	
	i = len(sep_name_u)-1
	if i > -1:
		a = sep_name_u[i] 
		if i > 0:	
			b = sep_name_u[i-1]
			x = b + a #mg
			if x in symbols:
				sname.append(elements[symbols.index(x)])
				sep_name_u.pop()
				sep_name_u.pop()
				write_symbol_name(sep_name_u, sname)
			elif a in symbols:
				sname.append(elements[symbols.index(a)])
				sep_name_u.pop()
				write_symbol_name(sep_name_u, sname)			
			else:	
				sname.append('0')
		elif a in symbols:
			sname.append(elements[symbols.index(a)])
		else:
			sname.append('0')
	return(sname)	


print('Would you like to enter a name? (y/n)')
while input().lower() == 'y':
	print('Please enter a name.')
	symbol_name = []
	name = input()
	sname = write_symbol_name(separate_name(name), symbol_name)
	sname.reverse()
	if '0' not in sname:
		images_list = []
		for x in sname:
			images_list.append(x[3])
		final_im = display_image(images_list)
		final_im.show()
	elif '0' in sname:
		print("Sorry, this name can't be printed with element symbols")
	print('Would you like to enter another name?')
print('Ok, goodbye.')







