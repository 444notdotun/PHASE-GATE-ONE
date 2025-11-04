def element_is_palindrome():
	my_element  = ["madam", "kali", "hello", "noon"]
	count = 0
	for elements in my_element:
		pals = ""
		for element in elements:
			pals = element + pals
		if elements == pals:
			my_element[count] = True;
		else:
			my_element[count] = False;
		count+=1
	return my_element
print(element_is_palindrome())