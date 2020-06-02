
from random import random, randint
import math

ACCURACY = 100

def decimal_provider(k, n):
	guess = 1
	minimum = 0
	for i in range(ACCURACY):
		random_select = minimum + random()*(guess - minimum)

		if (k + random_select)**2 == n:
			return random_select
		elif (k + random_select)**2 > n:
			guess = random_select
		else:
			minimum = random_select

	return guess

def zeros(n):
	index = str(n).find('.') + 1
	return len(str(n)[index:]) - 1

def root(n):
	assert n >= 0

	if type(n) == type(0.1) and str(n)[-1] != 0:
		if str(n)[0] == '0':
			return decimal_provider(0, n)

		return root(int(str(n).replace('.', '')))*decimal_provider(0,
		 float('0.' + '0'*(zeros(n))+'1'))

	minimum = 0
	maximum = int(math.ceil(n/2.0))
	guess = 0

	if n < 4:
		for i in range(0, n+1):
			if i*i == n:
				return i
			elif i*i > n:
				guess = i-1
				break
		return guess + decimal_provider(guess, n)

	while maximum - minimum != 1:
		random_select = randint(minimum, maximum)
		
		if random_select**2 == n:
			return random_select
		elif random_select**2 > n:

			maximum = random_select
		elif random_select**2 < n:
			minimum = random_select

	return minimum + decimal_provider(minimum, n)


