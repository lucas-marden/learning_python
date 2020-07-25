#a script to learn how to use regular expression parsing
#goal = find and replace, like 'command f'
import pdb
import re
import sys


def find(input, text):
	p = re.compile('(.*?)({})(.*)'.format(input), re.I | re.DOTALL)
	matches = p.search(text)
	if matches:
		return matches
	else:
		return None

def recombine(matches, seen):
	first_section = matches.group(1)
	key_word = matches.group(2)
	closing_section = matches.group(3)	
	one = '\033[0m{}'.format(first_section)
	two = '\033[33m{}'.format(key_word)
	three = '\033[0m{}'.format(closing_section)
	x = '{}{}{}{}'.format(seen,one,two,three)
	return x

def step(matches, previous):
	seen = previous + matches.group(1) + matches.group(2)
	next = matches.group(3)
	return seen, next;

for x in sys.argv[1:]:
	i = 0
	while i<1000:
		f = open(x, 'r')
		text = f.read()
		print('\033[0m{}'.format(text))
		print('\033[0mSearch:', end='')
		key = input()
		seen = ''
		a = 0
		while a<len(text):
			if find(key, text):
				print(recombine(find(key,text), seen))
				seen, next = step(find(key, text), seen)
				if input() == '':
					text = next
					a += 1
			else:
				break
		i += 1
	f.close()



