#this is an attempt to solve the problem using recursion, and return all possible symbol names

from usingclassforimg import list_elements_info
from usingclassforimg import symbols_list
from usingclassforimg import initial_elements
import pdb
from usingclassforimg import initial_elements
from combination import display_image
from PIL import Image
from itertools import combinations

elements = list_elements_info(initial_elements())
symbols = symbols_list(elements)


def separate_name(name):	
	name_u = name.upper()	
	sep_name_u = list(name_u)
	return sep_name_u

def write_symbols_list(sep_name_u):	
	symbols_list = []
	i = 0
	while i < len(sep_name_u):
		if i < len(sep_name_u)-1:
			if sep_name_u[i] + sep_name_u[i+1] in symbols:
				symbols_list.append(sep_name_u[i] + sep_name_u[i+1])
		if sep_name_u[i] in symbols:
			symbols_list.append(sep_name_u[i])
		i += 1
	return(symbols_list)		

def make_all_combos(symbols_list):
	all_combos = []
	i = 1
	while i < len(symbols_list):
		all_combos.extend(list(combinations(symbols_list, i)))
		i += 1 
	combos_no_dup = list(dict.fromkeys(all_combos))
	return(combos_no_dup)

def find_names(all_combos, name):
	names = []
	for x in all_combos:
		str = ''
		attempt = str.join(x)
		if attempt == name.upper():
			names.append(list(x))	
	return(names)

def show_image(sname, choice):
	images_list = []
	for x in sname[choice]:
		z = elements[symbols.index(x)]
		images_list.append(z[3])
	final_im = display_image(images_list)
	return final_im

print('Would you like to enter a name? (y/n)')
while input().lower() == 'y':
	print('Please enter a name.')
	name = input()
	sname = find_names(make_all_combos(write_symbols_list(separate_name(name))), name)
	print(sname)
	if len(sname) > 1:
		print(('There are {} options for this name.'.format(len(sname))))
		print('Which name would you like to display?(0,1,...)')
		choice = int(input())
		final_im = show_image(sname, choice)
		final_im.show()	
	elif len(sname) == 1:
		print('There is only 1 option for this name.')
		final_im = show_image(sname, 0)
		final_im.show()
	elif len(sname) == 0:
		print("Sorry, this name can't be spelled with the element symbols.")	
	print('Would you like to enter another name?')
print('Ok, goodbye.')







