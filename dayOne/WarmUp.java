public class WarmUp{

	public static int warmUpFunction(int input){
		double count = 1;
		int counter=0;
		int fixedPrice=50000;
		double newPrice = 0;
		newPrice = input*fixedPrice;

	while(count  >= 0.1){
	System.out.println(newPrice);
		double depValue=0.08;
		newPrice=newPrice*depValue;
		count = newPrice;
		
		
		counter++;
	
		}
	
	return counter;

}

public static void main(String...args){
System.out.print(warmUpFunction(100));


}
}



	