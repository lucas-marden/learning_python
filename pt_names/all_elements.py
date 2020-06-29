#this is a program to write names/strings of letters using elemental symbols

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

initial_elements = [
'H - Hydrogen',
'He - Helium',
'Li - Lithium',
'Be - Beryllium',
'B - Boron',
'C - Carbon',
'N - Nitrogen',
'O - Oxygen',
'F - Fluorine',
'Ne - Neon',
'Na - Sodium',
'Mg - Magnesium',
'Al - Aluminum',
'Si - Silicon',
'P - Phosphorus',
'S - Sulfur',
'Cl - Chlorine',
'Ar - Argon',
'K - Potassium',
'Ca - Calcium',
'Sc - Scandium',
'Ti - Titanium',
'V - Vanadium',
'Cr - Chromium',
'Mn - Manganese',
'Fe - Iron',
'Co - Cobalt',
'Ni - Nickel',
'Cu - Copper',
'Zn - Zinc',
'Ga - Gallium',
'Ge - Germanium',
'As - Arsenic',
'Se - Selenium',
'Br - Bromine',
'Kr - Krypton',
'Rb - Rubidium',
'Sr - Strontium',
'Y - Yttrium',
'Zr - Zirconium',
'Nb - Niobium',
'Mo - Molybdenum',
'Tc - Technetium',
'Ru - Ruthenium',
'Rh - Rhodium',
'Pd - Palladium',
'Ag - Silver',
'Cd - Cadmium',
'In - Indium',
'Sn - Tin',
'Sb - Antimony',
'Te - Tellurium',
'I - Iodine',
'Xe - Xenon',
'Cs - Cesium',
'Ba - Barium',
'La - Lanthanum',
'Ce - Cerium',
'Pr - Praseodymium',
'Nd - Neodymium',
'Pm - Promethium',
'Sm - Samarium',
'Eu - Europium',
'Gd - Gadolinium',
'Tb - Terbium',
'Dy - Dysprosium',
'Ho - Holmium',
'Er - Erbium',
'Tm - Thulium',
'Yb - Ytterbium',
'Lu - Lutetium',
'Hf - Hafnium',
'Ta - Tantalum',
'W - Tungsten',
'Re - Rhenium',
'Os - Osmium',
'Ir - Iridium',
'Pt - Platinum',
'Au - Gold',
'Hg - Mercury',
'Tl - Thallium',
'Pb - Lead',
'Bi - Bismuth',
'Po - Polonium',
'At - Astatine',
'Rn - Radon',
'Fr - Francium',
'Ra - Radium',
'Ac - Actinium',
'Th - Thorium',
'Pa - Protactinium',
'U - Uranium',
'Np - Neptunium',
'Pu - Plutonium',
'Am - Americium',
'Cm - Curium',
'Bk - Berkelium',
'Cf - Californium',
'Es - Einsteinium',
'Fm - Fermium',
'Md - Mendelevium',
'No - Nobelium',
'Lr - Lawrencium',
'Rf - Rutherfordium',
'Db - Dubnium',
'Sg - Seaborgium',
'Bh - Bohrium',
'Hs - Hassium',
'Mt - Meitnerium',
'Ds - Darmstadtium',
'Rg - Roentgenium',
'Cn - Copernicium',
'Nh - Nihonium',
'Fl - Flerovium',
'Mc - Moscovium',
'Lv - Livermorium',
'Ts - Tennessine',
'Og - Oganesson'
]
elements = []
i = 1
for x in initial_elements:
	new_item = x.split(" - ")
	new_item.append(i)
	elements.append(new_item)
	i += 1

#elements = [symbol, name, atomic number]





from element_class import Element

sl_elements = []
sl_symbols = []
tl_elements = []
tl_symbols = []
tl_symbols_u = []

for x in elements:
	e = Element(x[0], x[1], x[2])
	if len(e.symbol) == 1:
		sl_elements.append([e.symbol, e.name, e.number])
		sl_symbols.append(e.symbol)
	else:
		tl_elements.append([e.symbol, e.name, e.number])
		tl_symbols.append(e.symbol)
		tl_symbols_u.append(e.symbol.upper())
print('Enter your name')
name = input()
name_u = name.upper()
sep_name_u = list(name_u)

i = 0
while i < len(name_u)-1:	
	x = sep_name_u[i]
	y = sep_name_u[i+1]
	z = x + y
	if x in sl_symbols and z in tl_symbols_u:
		if y in sl_symbols:
			print(sl_elements[sl_symbols.index(x)])
		else:
			print(tl_elements[tl_symbols_u.index(z)])
			i += 1
	elif x in sl_symbols and z not in tl_symbols_u:
		print(sl_elements[sl_symbols.index(x)])
	elif z in tl_symbols_u and x not in sl_symbols:
		print(tl_elements[tl_symbols_u.index(z)])
		i += 1
	else:
		break
	i += 1
if i < len(name_u):
	x = sep_name_u[i]
	if x in sl_symbols:
		print(sl_elements[sl_symbols.index(x)])
	else:
		print("Sorry, your name can't be written with the elements of the period table")




