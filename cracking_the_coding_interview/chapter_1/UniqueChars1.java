import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class UniqueChars1 {
	
	public static boolean uniqueChars1(String str) {
		Set<Character> set = new HashSet<Character>();
		
		for (int i = 0; i < str.length(); i++) {
			char c = str.charAt(i);
			
			if (set.contains(c)) {
				return false;
			}
			set.add(c);
		}
		
		return true;
	}
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		while (input.hasNextLine()) {
			System.out.println(uniqueChars1(input.nextLine()) ? 1 : 0);
		}
	}
}