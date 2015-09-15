import java.util.Scanner;

class HelloBeatles {

    public static void main(String[] args) {
	Scanner input = new Scanner(System.in);

	while (input.hasNextLine()) {
	    System.out.println("Hello, " + input.nextLine() + "!");
	}
    }
}
