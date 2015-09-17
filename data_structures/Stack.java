// Based on Introduction to Algorithms, 2nd edition, Section 10.1.

import java.lang.Exception;

public class Stack {

	protected int top;
	protected int[] array;

	public Stack(int capacity) {
		top = -1;
		array = new int[capacity];
	}

	public boolean empty() {
		return top == -1;
	}

	public void push(int elem) throws OverflowException {
		if (top == array.length - 1) {
			throw new OverflowException();
		} else {
			array[++top] = elem;
		}
	}

	public int pop() throws UnderflowException {
		if (top == -1) {
			throw new UnderflowException();
		} else {
			return array[top--];
		}
	}

	public static class OverflowException extends Exception {}

	public static class UnderflowException extends Exception {}

	public static void main(String[] args) throws OverflowException, UnderflowException {
		Stack s = new Stack(7);
		s.push(15);
		s.push(6);
		s.push(2);
		s.push(9);
		s.push(17);
		s.push(3);
		s.pop();

		System.out.println(s.pop());
		System.out.println(s.pop());
		System.out.println(s.pop());
		System.out.println(s.pop());
		System.out.println(s.pop());
		if (s.empty()) {
			System.out.println("The stack is empty.");
		}
	}
}