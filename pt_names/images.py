#this is a program to write names/strings of letters using elemental symbols
from  usingclassforimg import list_elements_info
from usingclassforimg import symbols_list
from usingclassforimg import initial_elements
from combination import display_image
from PIL import Image

elements = list_elements_info(initial_elements())
symbols = symbols_list(elements)


def print_name(name):
#	pdb.set_trace()
	sname = []
	name_u = name.upper()
	sep_name_u = list(name_u)
	i = 0
	while i < len(name_u):
		a = sep_name_u[i]  #m
		if i < len(name_u)-1:	
			b = sep_name_u[i+1] #g
			x = a + b #mg
			if a in symbols:
				if x in symbols:
					if i < len(name_u)-2:
						c = sep_name_u[i+2] #a
						y = b + c #ga
						if y in symbols:
							if i < len(name_u)-3:
								d = sep_name_u[i+3]
								z = c + d
								if d in symbols and z not in symbols:
									sname.append(elements[symbols.index(a)])
									sname.append(elements[symbols.index(y)])
									i += 2
								if d not in symbols and z in symbols:
									sname.append(elements[symbols.index(x)])
									i += 1
	final_im.show()
								if d in symbols and z in symbols:
									sname.append(elements[symbols.index(x)])
									i += 1
							elif i == len(name_u)-3:
								sname.append(elements[symbols.index(a)])
								sname.append(elements[symbols.index(y)])
								i += 2
						if c in symbols and y not in symbols:
							sname.append(elements[symbols.index(x)])
							i += 1
						if c not in symbols and y in symbols:
							sname.append(elements[symbols.index(a)])
					elif i == len(name_u)-2:
						sname.append(elements[symbols.index(x)])
						i += 1
				elif x not in symbols:
					sname.append(elements[symbols.index(a)])
			elif x in symbols and a not in symbols:
				sname.append(elements[symbols.index(x)])
				i += 1
			elif x not in symbols and a not in symbols:
				sname.append('💩')
				break
		elif i == len(name_u)-1:
			if a in symbols:
				sname.append(elements[symbols.index(a)])
			else:
				sname.append('💩')
		i += 1
	return sname			

print('Would you like to enter a name?(Y/N)')
while input().upper() == 'Y':	
	print('Enter a name')
	sname = print_name(input().upper())
	if '💩' not in sname:
		images_list = []
		for x in sname:
			images_list.append(x[3])
		final_im = display_image(images_list)
		final_im.show()
	else:
		print("Sorry, your name can't be written with the symbols of the elements")
	print('Would you like to enter another name?(Y/N)')
print('Ok, goodbye.')


