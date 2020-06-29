#this is a script to calculate the factorial of any number using recursion


def factorial(k):
	if k > 1:
		result = k*factorial(k-1)
	else:
		result = 1
	return result


#print('Please enter a number.')
number = 10
print(factorial(number))


