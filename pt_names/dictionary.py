#this is a program to write names/strings of letters using elemental elements

elements = {
	'H': 'Hydrogen',
	'He': 'Helium',
	'Li': 'Lithium',
	'Be': 'Beryllium',
	'B': 'Boron',
	'C': 'Carbon',
	'N': 'Nitrogen',
	'O': 'Oxygen',
	'F': 'Fluorine',
	'Ne': 'Neon',
	'Na': 'Sodium',
	'Mg': 'Magnesium',
	'Al': 'Aluminum',
	'Si': 'Silicon',
	'P': 'Phosphorus',
	'S': 'Sulfur',
	'Cl': 'Chlorine',
	'Ar': 'Argon',
	'K': 'Potassium',
	'Ca': 'Calcium',
	'Sc': 'Scandium',
	'Ti': 'Titanium',
	'V': 'Vanadium',
	'Cr': 'Chromium',
	'Mn': 'Manganese',
	'Fe': 'Iron',
	'Co': 'Cobalt',
	'Ni': 'Nickel',
	'Cu': 'Copper',
	'Zn': 'Zinc',
	'Ga': 'Gallium',
	'Ge': 'Germanium',
	'As': 'Arsenic',
	'Se': 'Selenium',
	'Br': 'Bromine',
	'Kr': 'Krypton',
	'Rb': 'Rubidium',
	'Sr': 'Strontium',
	'Y': 'Yttrium',
	'Zr': 'Zirconium',
	'Nb': 'Niobium',
	'Mo': 'Molybdenum',
	'Tc': 'Technetium',
	'Ru': 'Ruthenium',
	'Rh': 'Rhodium',
	'Pd': 'Palladium',
	'Ag': 'Silver',
	'Cd': 'Cadmium',
	'In': 'Indium',
	'Sn': 'Tin',
	'Sb': 'Antimony',
	'Te': 'Tellurium',
	'I': 'Iodine',
	'Xe': 'Xenon',
	'Cs': 'Cesium',
	'Ba': 'Barium',
	'La': 'Lanthanum',
	'Ce': 'Cerium',
	'Pr': 'Praseodymium',
	'Nd': 'Neodymium',
	'Pm': 'Promethium',
	'Sm': 'Samarium',
	'Eu': 'Europium',
	'Gd': 'Gadolinium',
	'Tb': 'Terbium',
	'Dy': 'Dysprosium',
	'Ho': 'Holmium',
	'Er': 'Erbium',
	'Tm': 'Thulium',
	'Yb': 'Ytterbium',
	'Lu': 'Lutetium',
	'Hf': 'Hafnium',
	'Ta': 'Tantalum',
	'W': 'Tungsten',
	'Re': 'Rhenium',
	'Os': 'Osmium',
	'Ir': 'Iridium',
	'Pt': 'Platinum',
	'Au': 'Gold',
	'Hg': 'Mercury',
	'Tl': 'Thallium',
	'Pb': 'Lead',
	'Bi': 'Bismuth',
	'Po': 'Polonium',
	'At': 'Astatine',
	'Rn': 'Radon',
	'Fr': 'Francium',
	'Ra': 'Radium',
	'Ac': 'Actinium',
	'Th': 'Thorium',
	'Pa': 'Protactinium',
	'U': 'Uranium',
	'Np': 'Neptunium',
	'Pu': 'Plutonium',
	'Am': 'Americium',
	'Cm': 'Curium',
	'Bk': 'Berkelium',
	'Cf': 'Californium',
	'Es': 'Einsteinium',
	'Fm': 'Fermium',
	'Md': 'Mendelevium',
	'No': 'Nobelium',
	'Lr': 'Lawrencium',
	'Rf': 'Rutherfordium',
	'Db': 'Dubnium',
	'Sg': 'Seaborgium',
	'Bh': 'Bohrium',
	'Hs': 'Hassium',
	'Mt': 'Meitnerium',
	'Ds': 'Darmstadtium',
	'Rg': 'Roentgenium',
	'Cn': 'Copernicium',
	'Nh': 'Nihonium',
	'Fl': 'Flerovium',
	'Mc': 'Moscovium',
	'Lv': 'Livermorium',
	'Ts': 'Tennessine',
	'Og': 'Oganesson'
}






import pdb
import sys



def print_name(name):
#	pdb.set_trace()
	sname = []
	name_u = name.upper()
	sep_name_u = list(name_u)
	i = 0
	while i < len(name_u):
		a = sep_name_u[i]  
		if i < len(name_u)-1:	
			b = sep_name_u[i+1]
			x = a + b.lower() 
			if a in elements:
				if x in elements:
					if i < len(name_u)-2:
						c = sep_name_u[i+2] 
						y = b + c.lower()
						if y in elements:
							if i < len(name_u)-3:
								d = sep_name_u[i+3]
								z = c + d.lower()
								if d in elements and z not in elements:
									sname.extend([a, elements[a]])
									sname.extend([y, elements[y]])
									i += 2
								if d not in elements and z in elements:
									sname.extend([x, elements[x]])
									i += 1
								if d in elements and z in elements:
									sname.extend([x, elements[x]])
									i += 1
							elif i == len(name_u)-3:
								sname.extend([a, elements[a]])
								sname.extend([y, elements[y]])
								i += 2
						if c in elements and y not in elements:
							sname.extend([x, elements[x]])
							i += 1
						if c not in elements and y in elements:
							sname.extend([a, elements[a]])
					elif i == len(name_u)-2:
						sname.extend([x, elements[x]])
						i += 1
				elif x not in elements:
					sname.extend([a, elements[a]])
			elif x in elements and a not in elements:
				sname.extend([x, elements[x]])
				i += 1
			elif x not in elements and a not in elements:
				sname.append('💩')
				break
		elif i == len(name_u)-1:
			if a in elements:
				sname.extend([a, elements[a]])
			else:
				sname.append('💩')
		i += 1
	return sname			


"""
for name in sys.argv[1:]:
	print(name)
	sname = print_name(name.upper())
	if '💩' not in sname:
		print(sname)
	else:
		print("{} cannot be expressed in elements".format(name))
"""

print('Would you like to enter a name?(Y/N)')
while input().upper() == 'Y':	
	print('Enter a name')
	sname = print_name(input().upper())
	if '💩' not in sname:
		print(sname)
	else:
		print("Sorry, your name can't be written with the elements of the elements")
	print('Would you like to enter another name?(Y/N)')
print('Ok, goodbye.')

"""
for name in [line.strip() for line in sys.stdin.readlines()]:
	print(name)
	sname = print_name(name.upper())
	if '💩' not in sname:
		print(sname)
	else:
		print("{} cannot be expressed in elements".format(name))

"""
