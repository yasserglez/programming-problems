// https://www.hackerrank.com/challenges/tree-preorder-traversal

import java.util.ArrayDeque;

class TreePreorderTraversal {

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

    static void Preorder(Node root) {
        ArrayDeque<Node> stack = new ArrayDeque<Node>();

        if (root != null) stack.addFirst(root);

        while (!stack.isEmpty()) {
            Node node = stack.removeFirst();
            System.out.print(node.data + " ");
            if (node.right != null) stack.addFirst(node.right);
            if (node.left != null) stack.addFirst(node.left);
        }
    }

    public static void main(String[] args) {
        Node root = new Node(3);
        root.left = new Node(5);
        root.left.left = new Node(1);
        root.left.right = new Node(4);
        root.right = new Node(2);
        root.right.left = new Node(6);

        Preorder(root);
    }
}
