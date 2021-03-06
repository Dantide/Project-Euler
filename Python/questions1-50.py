from common import *

#Problem Solving Area

#print (timeit.repeat("for x in range(100): factor(x)", "from __main__ import factor", number=1000))
#print (timeit.repeat("for x in range(100): factor2(x)", "from __main__ import factor2", number=1000))
print ("running")

#problem 1 SOLVED
def problem1():
  "Find the sum of all multiples of 3 or 5 below 1000."
  count = 0
  for x in range(0, 1000):
    if (x % 3 == 0) or (x % 5 == 0):
      count += x
  print (count)

#problem 2 SOLVED
def fibiter2():
  "Find the sum of all even fibbonacci numbers below four million."
  i, count = 0, 0
  num = fibnum(i)
  while (num < 4000000):
    if (num % 2 == 0):
      count += num
    i += 1
    num = fibnum(i)
  print (count)

#problem 3 SOLVED
def problem3():
  "Find the largest prime factor of 600851475143."
  array = []
  temp = 600851475143
  while not isPrime(temp):
    for x in range(2,int(temp**0.5) + 1):
      if isPrime(x) and (temp % x == 0):
        array.append(x)
        temp /= x
        break
  array.append(int(temp))
  array.sort()
  return (array)

#problem 4 SOLVED
def isPalindrome(n):
  "Tests if a number is a palindrome."
  if str(n) == str(n)[::-1]:
    return True
  else:
    return False

def largestpalinproduct(digits):
  "A more general code for problem 4, but it is not very efficient. It works though."
  array = []
  largest = 10**digits
  smallest = 10**(digits - 1)
  for x in range(largest - 1, smallest, -1):
    for i in range(largest - 1, smallest, -1):
      temp = x*i
      if isPalindrome(temp):
        array.append(temp)
  else:
    return max(array)

def problem4():
  "Find the largest palindrome made from the product of two 2-digit numbers."
  for num in range(999, 700, -1):
    for x in range(999, 700, -1):
      temp = x*num
      if isPalindrome(temp):
        return temp

#problem 5 SOLVED
def problem5(n):
  "LCM of all numbers from 1 to n."
  most = {}
  pexpo = primeExpo
  pfactor = primeFactor
  for x in range(1, n):
    #Find the prime factors of all numbers from 1 to n.
    temp = pexpo(pfactor(x))
    testproblem5(temp, most)
  print (mult5(most))

def testproblem5(temp, most):
  "Just keeping most as the dictionary with the most occurrences of each prime factor."
  for x in temp:
    if not((x in most) and (temp[x] < most[x])):
      #The only time we don't run this code is if x is in both dictionaries
      #and temp[x] is less than most[x].
      most[x] = temp[x]

def mult5(most):
  "Multiply all the factors (to the power of the max times it appeared in one number) together."
  temp = 1
  for x in most:
    temp *= x**most[x]
  return temp

#problem 7 SOLVED
def problem7():
  numprime = 10001 # The number prime that we want to find (i.e. 3 if want 3rd prime)
  count = 1 # Start at 1, skip 2 as a prime
  x = 3  # Start at 3, skip 2 as a prime
  while count < numprime:
    if isPrime(x):
      count+=1
    x+=2
  print (x-2)

#problem 8 SOLVED
def multiply(lst):
  total = 1
  for l in lst:
    total *= l
  return total

def problem8():
  f = open(ASSETS_PATH + "problem8.txt")
  num_buffer = [0] * 13
  index, max_num = 0, 0
  string = ""
  for line in f:
    string = string + line
  for char in string:
    if (char != '\n'):
      num_buffer[index] = int(char)
      if multiply(num_buffer) > max_num:
        max_num = multiply(num_buffer)
      index = (index + 1) % 13
  print (max_num)

#problem 9 TODO
def problem9():
  return "wtf do I do"

#problem 10 SOLVED
def sumOfPrimesBelow(n):
  """ Brute Force Method """
  count = 0
  for x in range(3, n, 2):
    if isPrime(x):
      count += x
  return count + 2

def sieveArrays(n):
  """ Inspired by Sieve of Eratosthenes, also a brute force method """
  primes = [2, 3, 5, 7]
  for num in range(11, n, 2):
    print(num)
    if next((False for p in primes if num % p == 0), True):
      primes.append(num)
  return sum(primes)

def problem10():
  print(sieveArrays(2000000))

problem10()

#problem 12 SOLVED
def factor(n):
  "Return an array with all the factors of a number. Load increases greatly when using large numbers."
  if n <= 0:
    return None
  array = [1, n]
  for x in range(2, int(n**0.5)):
    if (n % x == 0):
      array.append(x)
      array.append(int(n/x))
  array.sort()
  return array

def factor2(n):
  if n <= 0:
    return None
  array = []
  for x in [x for x in range(1, int(n**0.5)) if (n % x == 0)]:
    array.append(x)
    array.append(int(n/x))
  array.sort()	
  return array

def problem12(n):
  "Find the first number in the range that has more than n factors."
  fact = factor
  tri = triNum
  for x in [tri(i) for i in range(11000, 13000)]:
    num2 = len(fact(x))
    if num2 >= n:
      print (num2)
      return x
  else:
    return None


#problem 13 SOLVED
def problem13():
  "Find the first 10 digits of the sum of the following one-hundred 50-digit numbers."
  thing = open("C:/Users/Stephen/Desktop/projecteuler/problem 13.txt")
  num = 0
  for line in thing:
    num += int(line)
  print (num)
  thing.close()

#problem 15 SOLVED
def findLattice(n):
  "Return # of lattice paths in box n by n. http://www.mozartreina.com/counting-lattice-paths.html"
  array = [[1 for x in range(n+1)] for x in range(n+1)]
  for x in range(1, n+1):
    first = True
    for i in range(x, n+1):
      if first:
        array[x][i] = array[x-1][i] * 2
        first = False
      else:
        array[x][i] = array[x-1][i] + array[x][i-1]
  else:
    return array[len(array)-1][len(array)-1]

#problem 18
def test18():
  "Test"
  f = open(ASSETS_PATH + r'test18.txt')
  f.close()

def problem18():
  """
  Choose from the larger of the next two numbers. The implementation was correct,
  but the idea was wrong.
  """
  f = open(ASSETS_PATH + r'problem18.txt')
  print (findmaximumpath(f))
  f.close()

def findmaximumpath(f):
  for line in f:
    print(line)


#problem 20 SOLVED
#print (sumDigits(factorial(10)))

#problem 22 SOLVED
def problem22():
  "What is the total of all the name scores in the file? (In alphabetical order)"
  temp, count = 0, 1
  f = open("C:/Users/Stephen/Desktop/projecteuler/p022_names.txt")
  thing = string.punctuation
  for i in f:
    array = i.split(',')
    array.sort()
  for word in array:
    for letter in word:
      if (letter not in thing) and (letter is not ""):
        temp += (letterdict[letter] * count)
    count += 1
  print (temp)

#problem 25 SOLVED
def problem25():
  "Return the n index of the first fibbonacci number longer than 1000 digits."
  i = 1
  while True:
    if len(str(fibnum(i))) == 1000:
      return i
    else:
      i += 1

#problem 28 SOLVED
def createSpiral(n):
  if (n%2 == 0):
    return None
  array = [[0 for x in range(n)] for x in range(n)]

  for i in array:
    print (i)

def addSpiralDiag(n):
  "Adds all the numbers on the diagonals of an n by n array."
  if (n%2 == 0):
    return None
  num = 1 					#the diagonal number to be added to count
  count = num 				#has the total to be returned later
  numofdiags = 2*n - 1 		#number of diagonal numbers in the array
  for i in range(1, numofdiags):

    inc = int((i+3)/4)*2 	#Every four numbers, the space between the diagonal numbers increases by two
    num += inc 				#The next diagonal number to add to count
    count += num
  return count
