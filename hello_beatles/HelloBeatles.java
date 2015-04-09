import java.util.Scanner;

class HelloBeatles {

    public static void main(String[] args) {
	Scanner input = new Scanner(System.in);

	while (input.hasNext()) {
	    System.out.println("Hello, " + input.next() + "!");
	}
    }
}
