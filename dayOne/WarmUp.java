public class WarmUp{

	public static int WarmUpFunction(int input){
		double count = 1;
		int counter=0;
		int fixedPrice=50000;
		double newPrice = 1.0;
	while(count > 0){
		newPrice = input*fixedPrice;
	
		double depValue=0.08;
		count=newPrice/depValue;
		counter++;
	
		}
	
return counter;

}
}	