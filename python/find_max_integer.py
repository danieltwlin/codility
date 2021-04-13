def find_min_positive(nums):
	s = set(nums)
	i=1
	while i in s:
		i = i + 1
	return i
	
	
if __name__=='__main__':

	nums =[1, 3, 6, 4, 1, 2]
	max = find_min_positive(nums)
	print(max)
	
	nums = [1, 2, 3]
	max = find_min_positive(nums)
	print(max)
	
        nums = [1, 2, 3]
	max = find_min_positive(nums)
	print(max)
  
	nums =  [−1, −3]
	max = find_min_positive(nums)
	print(max)
 
