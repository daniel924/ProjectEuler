from random import random

def swap(a, left, right):
	temp = a[left]
	a[left] = a[right]
	a[right] = temp


#partition all items less than pivot to the left,
#and all items greater to the right
def partition(a,left,right,pivot):
	
	if left == right:
		return
			
	if a[left] >= pivot and a[right] <= pivot:
		swap(a, left, right)

	if a[left] < pivot:
		return partition(a, left + 1, right, pivot)
	
	if a[right] > pivot:
		return partition(a, left, right - 1, pivot)
	

#pick a partition, partition over pivot, and 
#recursively apply to both sides 
def qSort1(a, left, right):
		
	if right - left < 1:
		return
	
	pivot = a[ int( random() % ( right - left+1) ) + left ] 	
	
	partition(a,0, right, pivot)

	#find partition
	pIndex = a.index(pivot)
	
	#partition both subawways
	qSort1(a,left, pIndex-1)
	
	qSort1(a, pIndex + 1, right)

	
#quicksort - sorts an array 
#@params a - an array to be sorted
def qSort(a):
	qSort1(a, 0, len(a)-1)
	
	
	
a = [5,86,69,73,11,17,1,74,34,3]

qSort(a)
print a		
			
			
	
	
	
	


