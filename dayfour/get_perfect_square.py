def get_square():
	test_list = [4,6,49,25]
	
	array = [0,0,0,0]
	for counting in range(0,4):
		count = 0
		number = test_list[counting]
		
		counter = 0

		while number > 0:
			
			if counter % 2 > 0:
				number-=counter
				count+=1
				
			counter+=1
		print(count)
		if count*count == test_list[counting]: 
			array[counting]=True
				
		else:
			array[counting]=False
		if test_list[counting]==0:
			array[counting]=False
				

	return array

print(get_square())
		
		
	
