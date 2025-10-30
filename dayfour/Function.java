public class Function{

	public static Boolean[] get_perfect_square(){
	int [] test_list={4,6,25,49,100};
	Boolean [] array = new Boolean [4];
        for (int count = 0; count < test_list.length; count++) {
		
            int number = test_list[count];
             	int divisor = 2;
		
		
                while(number % divisor != 0) {
                    	divisor++;

                }
		int dividedIndex = number / divisor;
		
               	if (number == dividedIndex * dividedIndex) {
                	array[count] = true;
            	}else{
                	array[count] = false;
            	}
		}
		
		return array;
	}

}

 