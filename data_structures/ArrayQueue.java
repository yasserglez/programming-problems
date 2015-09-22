
// Based on Introduction to Algorithms, 2nd edition, Section 10.1.

import java.lang.Exception;

public class ArrayQueue {

    protected int head, tail;
    protected int[] array;

    public ArrayQueue(int capacity) {
        head = 0;
        tail = 0;
        array = new int[capacity + 1];
    }

    public void enqueue(int elem) throws OverflowException
    {
        if (tail == head - 1 || (tail == array.length - 1 && head == 0)) {
            throw new OverflowException();
        } else {
            array[tail] = elem;
            if (tail == array.length - 1) {
                tail = 0;
            } else {
                tail++;
            }
        }
    }

    public int dequeue() throws UnderflowException
    {
        if (head == tail) {
            throw new UnderflowException();
        } else {
            int elem = array[head];
            if (head == array.length - 1) {
                head = 0;
            } else {
                head++;
            }
            return elem;
        }
    }

    public static class OverflowException extends Exception {
    }

    public static class UnderflowException extends Exception {
    }

    public static void main(String[] args) throws OverflowException, UnderflowException
    {
        ArrayQueue q = new ArrayQueue(11);
        for (int i = 0; i < 6; i++) {
            q.enqueue(0);
            q.dequeue();
        }
        q.enqueue(15);
        q.enqueue(6);
        q.enqueue(9);
        q.enqueue(8);
        q.enqueue(4);

        q.enqueue(17);
        q.enqueue(3);
        q.enqueue(5);
        q.dequeue();

        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
        System.out.println(q.dequeue());
    }
}
