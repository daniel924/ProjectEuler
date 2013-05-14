#Daniel Ladenheim

#A permutation is an ordered arrangement of objects. 
#For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
#If all of the permutations are listed numerically or alphabetically, 
#we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
#012   021   102   120   201   210
#
#What is the millionth lexicographic permutation 
#of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
#http://projecteuler.net/problem=24

import sys
import time

#swap indexes i and j in the array p
def swap(p, i,j):
	temp = p[j]
	p[j] = p[i]
	p[i] = temp


#finds next lexographical permutation
def getNextPerm(p):
	z = len(p) - 1
	
	oldDisp = 1
	disp = 0
	
	
	#find number to be swapped	
	while( p[z - disp-1] > p[z-disp] ):	
		disp = disp + 1
		
	#start by swapping from back, and moving forward	
	if disp == 0: 	
		swap(p, z-1, z )
		return p
	else:
		for i in reversed( range(0, len(p) ) ):
			if p[i] > p[z - disp-1]:
				swap(p, z-disp-1, i)
				break
		
		#reset lower numbers to original positions			
		a = p[:z-disp]
		b = p[z-disp:]
		b.sort()
		
		return a + b	



st = time.time()

#using p as base case, find 1,000,000th permutation
p = [0,1,2,3,4,5,6,7,8,9]
for i in range(1,1000000):
	p = getNextPerm(p)
	
print ''.join( [str(x) for x in p  ] ) 
print "time = " + `time.time()-st`
