// Based on Introduction to Algorithms, 2nd edition, Chapter 12.

public class BinarySearchTree {
    int key;
    BinarySearchTree parent;
    BinarySearchTree left, right;
    
    public BinarySearchTree(int key) {
        this.key = key;
        parent = null;
        left = null;
        right = null;
    }
    
    public BinarySearchTree search(int key) {
        BinarySearchTree node = this;
        while (node != null && key != node.key) {
            if (key < node.key) {
                node = node.left;
            } else if (key > node.key) {
                node = node.right;
            }
        }
        return node;
    }

    public BinarySearchTree minimum() {
        BinarySearchTree node = this;
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    public BinarySearchTree maximum() {
        BinarySearchTree node = this;
        while (node.right != null) {
            node = node.right;
        }
        return node;
    }
    
    public BinarySearchTree successor() {
        if (this.right != null) {
            return this.right.minimum();
        } else {
            BinarySearchTree node = this.parent;
            while (node.parent != null && node.parent.left != node) {
                node = node.parent;
            }
            return node.parent;
        }
    }
    
    public BinarySearchTree predecessor() {
        if (this.left != null) {
            return this.left.maximum();
        } else {
            BinarySearchTree node = this.parent;
            while (node.parent != null && node.parent.right != node) {
                node = node.parent;
            }
            return node.parent;
        }
    }
    
    public void insert(int key) {
        insert(new BinarySearchTree(key));
    }
    
    public void insert(BinarySearchTree newNode) {
        BinarySearchTree node = this, parent = this.parent;
        while (node != null) {
            parent = node;
            if (newNode.key <= node.key) {
                node = node.left;
            } else {
                node = node.right;
            }
        }
        newNode.parent = parent;
        if (newNode.key <= parent.key) {
            assert parent.left == null;
            parent.left = newNode;                        
        } else {
            assert parent.right == null;
            parent.right = newNode;
        }
    }
    
    public BinarySearchTree delete(int key) {
        return delete(search(key));
    }
    
    public BinarySearchTree delete(BinarySearchTree node) {
        if (node.left != null && node.right != null) {
            // both left and right subtrees
            BinarySearchTree successor = node.successor();
            node.key = successor.key;
            if (successor.right == null) {
                if (successor.parent.left == successor) {
                    successor.parent.left = null;
                } else {
                    successor.parent.right = null;
                }
            } else {
                successor.key = successor.right.key;
                successor.left = successor.right.left;
                successor.right = successor.right.right;
                if (successor.left != null) {
                    successor.left.parent = successor;   
                }
                if (successor.right != null) {
                    successor.right.parent = successor;   
                }
            }
        } else if (node.left != null) {
            // left subtree, but no right subtree
            node.key = node.left.key;
            node.right = node.left.right;
            node.left = node.left.left;
        } else if (node.right != null) {
            // right subtree, but no left subtree
            node.key = node.right.key;
            node.left = node.right.left;
            node.right = node.right.right;
        } else {
            // no left or right subtrees
            if (node.parent == null) {
                assert node == this;
                return null;
            } else {
                if (node.parent.left == node) {
                    node.parent.left = null;
                } else {
                    node.parent.right = null;
                }
            }
        }
        // update node's parents
        if (node.left != null) {
            node.left.parent = node;   
        }
        if (node.right != null) {
            node.right.parent = node;   
        }
        
        return this;
    }

    private void print() {
        if (left != null) left.print();
        System.out.println(key);
        if (right != null) right.print();
    }

    public static void main(String[] args) {
        BinarySearchTree root = new BinarySearchTree(15);
        int[] others = {5, 3, 12, 10, 6, 7, 13, 16, 20, 18, 23};
        for (int i = 0; i < others.length; i ++) {
            root.insert(others[i]);
        }
        root.delete(13);
        root.delete(16);
        root.delete(6);
        root.print();
    }
}