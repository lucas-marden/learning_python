#a script to help me learn how to create a list of lists with recursion



def create_list_of(letters, list):
	i = 0
	while i < 25:
		if i < 24:
			if i < 23:
				new_item = [letters[i], letters[i+1], letters[i+2]]
			else:
				new_item = [letters[i], letters[i+1]]
		else:
			new_item = [letters[i]]
		list.append(new_item)
		i += 1
	return(list)

list = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(create_list_of(letters, list))


import sys
print(sys.getrecursionlimit())


