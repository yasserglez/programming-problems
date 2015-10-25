// https://www.hackerrank.com/challenges/tree-postorder-traversal

import java.util.ArrayDeque;

class TreePostorderTraversal {

    static class Node {
        int data;
        Node left;
        Node right;

        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    static void Postorder(Node root) {
        ArrayDeque<Node> stack = new ArrayDeque<Node>();
        if (root != null) stack.addFirst(root);
        Node current = null, previous;

        while (!stack.isEmpty()) {
            previous = current;
            current = stack.peekFirst();

            if (previous == null || current == previous.left) {
                // Traversing downwards.
                if (current.right != null) stack.addFirst(current.right);
                if (current.left != null) stack.addFirst(current.left);
            } else if (current.left == null && current.right == null) {
                // Leaf node.
                System.out.print(current.data + " ");
                stack.removeFirst();
            } else if (current.right == previous || current.left == previous) {
                // Traversing upwards.
                System.out.print(current.data + " ");
                stack.removeFirst();
            } else {
                // Finished with left sub-tree, switching to right sub-tree.
                if (current.right != null) stack.addFirst(current.right);
                if (current.left != null) stack.addFirst(current.left);
            }
        }
    }

    public static void main(String[] args) {
        Node root = new Node(3);
        root.left = new Node(5);
        root.left.left = new Node(1);
        root.left.right = new Node(4);
        root.right = new Node(2);
        root.right.left = new Node(6);

        Postorder(root);
    }
}
