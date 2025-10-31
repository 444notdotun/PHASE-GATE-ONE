function get_perfect_square(test_list){
	let array = []
	for (let count = 0; count < test_list.length; count++) {
		let counting = 0;
		
		let number=test_list[count];
		for(let counter = 0;number > 0; counter++){
			if (counter % 2 > 0){
				number-=counter;
				counting++;
			} 
			}
			
			if(counting*counting == test_list[count]) array[count]=true;	
			else array[count]=false;
			if (test_list[count]==0)array[count]=false;
				
			
			}
return array;
}
console.log(get_perfect_square([1,0,4,100,101]))
