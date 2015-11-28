// https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list

public class ReverseDoublyLinkedList {

    public static class Node {
        int data;
        Node next;
        Node prev;

        public Node(int data) {
            this.data = data;
            next = null;
            prev = null;
        }
    }

    // Time complexity: O(n)
    // Auxiliary space complexity: O(1)

    public static Node Reverse(Node head) {
        if (head == null) {
            return head;
        } else {
            Node curr, tmp;

            curr = head;
            while (curr.next != null) {
                tmp = curr.prev;
                curr.prev = curr.next;
                curr.next = tmp;
                curr = curr.prev;
            }
            curr.next = curr.prev;
            curr.prev = null;

            return curr;
        }
    }

    public static void print(Node head) {
        Node curr;

        curr = head;
        while (curr != null) {
            System.out.println(curr.data);
            curr = curr.next;
        }
    }

    public static void main(String[] args)
    {
        Node n2 = new Node(2), n4 = new Node(4), n6 = new Node(6);

        n2.next = n4;
        n4.prev = n2;
        n4.next = n6;
        n6.prev = n4;

        print(Reverse(n2));
    }
}
