function get_perfect_square(test_list){
	
	for (let count = 0; count < test_list.length; count++) {
		let counter = 2;
		if(test_list[count] <=1){
			test_list[count]=false;
			counter=0;
				}
		 
		while(counter !=0){
			let value = test_list[count]%counter;
			if (value == 0){
				let newvalue=test_list[count]/counter;
				if(newvalue*newvalue == test_list[count]){
					console.log(test_list[count])
					test_list[count]=true;
				}
				else{
					test_list[count]=false;
				}
				
				counter = value;
			}
			else{
				counter++;
			}
		}
	}
return test_list;
}
console.log(get_perfect_square([0,4,9,25,49,100,101]))
