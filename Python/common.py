#REOCCURING FUCTIONS
letterdict = {
	'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9,
  'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17,
  'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26
}

def isPrime(n):
	"""
  Test if number is prime. Returns True or False.

  Requires: [n] is a valid int.
  """
  assert (n is int)
	if (n < 2):
		return False
	if (n == 2) or (n == 5):
		return True
	if (n % 2 == 0) or (n % 5 == 0):
		return False
	for x in range(2, int(n/2)):
		if (n % x == 0):
			return False
	return True

def fibnum(n):
	"Returns the nth fibbonacci number, assuming that we go: 1, 1, 2, 3, 5, etc."
	if n==1 or n==2: return 1

	num1, num2, temp = 1, 1, 0
	for x in range(n-2):
		temp = num2
		num2 += num1
		num1 = temp
	return num2

def primeFactor(n):
	"Find the prime factors of a number."
	if n < 2: return []

	array = []
	temp = n
	isP = isPrime
	finished = isP(temp)
	while not finished:
		for x in range(2,int(temp**0.5) + 1):
			if isP(x) and (temp % x == 0):
				array.append(x)
				temp /= x
				break
		finished = isPrime(temp)
	array.append(int(temp))
	array.sort()
	return array

def primeExpo(arr):
	"The 'key' shows up 'value' amount of times in the dictionary."
	temp = {}
	for x in arr:
		if x not in temp:
			temp[x] = 1
		else:
			temp[x] += 1
	return temp

def factorial(n):
	"Return the factorial of n."
	temp = 1
	for x in range(1, n+1):
		temp *= x
	return (temp)

def sumDigits(n):
	"Return the sum of the digits in a number. sumDigits(87) = 8 + 7 = 15"
	temp = 0
	for x in str(n):
		temp += int(x)
	return temp

def triNum(n):
	"""Return the nth triangular number. Whereas t(n) = (n/2)(n+1)."""
	temp = (n/2)*(n+1)
	return int(temp)