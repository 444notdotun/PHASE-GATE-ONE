import java.util.Scanner;
	public class Main{
		public static void main(String...args){
		Scanner input = new Scanner(System.in);
		System.out.print("enter a number: ");
		int newInput = input.nextInt();
		System.out.print(WarmUpFunction(newInput));



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

}