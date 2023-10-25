package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class P0515 {
    public static List<Integer> largestValues(TreeNode<Integer> root) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        if (root == null) { 
            return res;
        }

        System.out.printf("Node val: %d%n", root.val);
        System.out.printf("Left Node val: %d%n", root.left.val);
        System.out.printf("Right Node val: %d%n", root.right.val);

        
        Stack<TreeNode<Integer>> current = new Stack<TreeNode<Integer>>();
        Stack<TreeNode<Integer>> next = new Stack<TreeNode<Integer>>();

        current.push(root);

        do {
            System.out.println("Iteration=====");
            System.out.printf("Current: %s%n", Arrays.toString(current.toArray()));
            System.out.printf("Next: %s%n", Arrays.toString(next.toArray()));
            int minValue = current.peek().val;
            while (!current.empty()) {
                TreeNode<Integer> node = current.pop();
                if (node.val > minValue) {
                    minValue = node.val;
                }
                if (node.left != null) {
                    next.push(node.left);
                }
                if (node.right != null) {
                    next.push(node.right);
                }
            }
            res.add(minValue);

            Stack<TreeNode<Integer>> temp = current;
            current = next;
            next = temp;
            System.out.printf("Current: %s%n", Arrays.toString(current.toArray()));
            System.out.printf("Next: %s%n%n", Arrays.toString(next.toArray()));
        } while (!current.empty());
        
        return res;
    }
}
