package leetcode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class TreeNode<T> {
    public T val;
    public TreeNode<T> left;
    public TreeNode<T> right;

    public TreeNode() {}
    public TreeNode(T val) {this.val = val;}
    public TreeNode(T val, TreeNode<T> left, TreeNode<T> right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public static<U> TreeNode<U> convertFromList(List<U> list) {
        if (list.isEmpty()) {
            return null;
        }

        TreeNode<U> root = new TreeNode<U>(list.get(0));
        LinkedList<TreeNode<U>> linkedList =  new LinkedList<TreeNode<U>>();
        linkedList.offer(root);
        boolean isLeft = true;
        for (int i = 1; i<list.size(); i++) {
            TreeNode<U> node = null;
            if (list.get(i) != null) {
                node = new TreeNode<U>(list.get(i));
            }
            linkedList.offer(node);
            if (isLeft) {
                linkedList.peek().left = node;
                isLeft = false;
            } else {
                linkedList.poll().right = node;
                isLeft = true;
            }
        }
        
        return root;
    }

    public boolean equals(TreeNode<T> other) {
        if (this == null && other == null) {
            return true;
        }
        if (this == null ^ other == null) {
            return false;
        }
        if (!this.val.equals(other.val)) {
            return false;
        }
        return this.left.equals(other.left) && this.right.equals(other.right);
    }

    
}
