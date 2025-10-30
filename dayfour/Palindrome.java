public class Palindrome{
	public static Boolean[] IsPalindrome(){
		String [] list={"madam", "kali", "hello", "noon"};
		Boolean[] Array = new Boolean[list.length];
			for(int count = 0; count < list.length; count++){
				String palindrome = "";

				for(int counter = 0; counter < list[count].length(); counter++){
					palindrome = list[count].charAt(counter) + palindrome;
				}

				if (list[count].equals (palindrome))
					Array[count] = true;
				else
					Array[count] = false;
			}
			return Array;
		
		}








}