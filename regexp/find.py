#a script to learn how to use regular expression parsing
#goal = find and replace, like 'command f'
import pdb
import re
import sys


def find(input, text):
	p = re.compile('(.*?)({})(.*)'.format(input), re.I | re.DOTALL)
	matches = p.search(text)
	return matches

def recombine(matches):
	first_section = matches.group(1)
	key_word = matches.group(2)
	closing_section = matches.group(3)	
	one = '\033[0;37;40m{}'.format(first_section)
	two = '\033[0;30;47m{}'.format(key_word)
	three = '\033[0;37;40m{}'.format(closing_section)
	x = '{}{}{}'.format(one,two,three)
	return x

def step(matches):
	seen = matches.group(1) + matches.group(2)
	next = matches.group(3)
	return seen, next;

for x in sys.argv[1:]:
	f = open('speech.txt', 'r')
	text = f.read()

	print('\033[0;47;40m{}'.format(text))
	print('Search:', end='')
	input = input()
	print(recombine(find(input,text)))
	seen, next = step(find(input, text))
	f.close()




