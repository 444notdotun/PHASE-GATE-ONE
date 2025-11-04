public class Function{
	public static Boolean[] get_perfect_square(){
	int [] test_list={81,0,25,49,100,7};
	Boolean [] array = new Boolean [test_list.length];
	
        for (int count = 0; count < test_list.length; count++){
		int counting = 0;
		int number=test_list[count];
		for(int counter = 0;number > 0; counter++){
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
}
	


		





 