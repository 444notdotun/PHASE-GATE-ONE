def get_square():
	number = {4,6,49,25}
	count = 0
	for counts in number:
		count+=1
	
	for counting in range(count):
		print(counting)
		counter =2
		while counter != 0:
			result = number[counting]%counter
			if result==0:
				actual = number[counting]/counter
				actual=actual*actual
			if actual== number[counting]:
					number[counting]=true
			else:
				 number[counting]= false
			counter = result	
			if number[count] == 0:
				array[count]=false
			
			if number[count] == 1:
				array[count]=true
				
			else:
				counter+=1
	return number

print(get_square())
		
		
	
