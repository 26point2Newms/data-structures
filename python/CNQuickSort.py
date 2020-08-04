'''
Created on Aug 3, 2020

@author: charles newman
https://github.com/26point2Newms
'''

def sort(lst):
	__quick(lst, 0, len(lst) - 1)

def __quick(lst, lb, ub):
	'''
	Recursive sort method.

	Arguments:
	lst : the list or array to sort
	lb	: the lower bound of the partition to sort
	ub	: the upper bound of the partition to sort
	'''

	if (lb >= ub):
		return
	
	pIndex = __partition(lst, lb, ub)

	__quick(lst, lb, pIndex - 1)

	__quick(lst, pIndex + 1, ub)

def __partition(lst, lb, ub):
	'''
	This function uses a pivot value, can be the lower bound,
	or the upper bound (see comments below). It places the 
	pivot value at its correct position in the sorted list by
	placing all values smaller than the pivot value to the
	left of the pivot value and all values greatter than the 
	pivot value to the right of the pivot value.

	Arguments:
	lst : the list or array to partition
	lb	: the lower bound of the partition
	ub	: the upper bound of the partition

	Returns:
	The partitioning index to use on subsequent calls
	'''
	# This is the pivot value, an area where we can experiment, such 
	#	as using the median of lst[lb], lst[ub], and the middle, lst[(lb+ub)/2].
	#	Or we can use lst[lb] or lst[up]
	# Pick one and comment the others out.
	# pivot = lst[lb]	# Using the lower bound as the pivot
	pivot = lst[ub]	# Using the upper bound as the pivot
	
	up = ub
	down = lb
	while (down < up):
		while (lst[down] <= pivot and down < ub):
			down += 1	# move up the array
		while (lst[up] > pivot):
			up -= 1		# move down the array
		if (down < up):
			# interchange lst[down] and lst[up]
			temp = lst[down]
			lst[down] = lst[up]
			lst[up] = temp
	lst[lb] = lst[up]
	lst[up] = pivot
	return up

