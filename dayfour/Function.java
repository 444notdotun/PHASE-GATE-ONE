public class Function{
	public static Boolean[] get_perfect_square(){
	int [] test_list={81,6,25,49,101,7};
	Boolean [] array = new Boolean [test_list.length];

        for (int count = 0; count < test_list.length; count++){
		int counter = 2; 
		while(counter !=0){
			int value = test_list[count]%counter;
			if (value == 0){
				int newvalue=test_list[count]/counter;
				if(newvalue*newvalue == test_list[count]){
					array[count]=true;
				}
				else{
					array[count]=false;
				}
				if(test_list[count] <=1){
					array[count]=false;
				}
				counter = value;
			}
			else{
				counter++;
			}
		}
	}
	return array;
}
}
	


		





 