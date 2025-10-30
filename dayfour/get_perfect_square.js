function get_perfect_square(test_list){
	
	for (let count = 0; count < test_list.length; count++) {
            let number = test_list[count];
             	let divisor = 2;

                while(number % divisor != 0) {
                    	divisor++;

                }
		let dividedIndex = number / divisor;
		
               	if (number == dividedIndex * dividedIndex) {
                	test_list[count] = true;
            	}else{
                	test_list[count] = false;
            	}
		}
		
return test_list;
}
console.log(get_perfect_square([4,9,25,49]))
