package leetcode;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class P0515Test {

    @Test
    void test1() {
        TreeNode<Integer> root = TreeNode.<Integer>convertFromList(Arrays.asList(1,3,2,5,3,null,9));
        List<Integer> expected_result = List.of(1,3,9);
        List<Integer> res = P0515.largestValues(root);

        assertEquals(expected_result, res);
    }

    @Test
    void test2() {
        TreeNode<Integer> root = TreeNode.<Integer>convertFromList(Arrays.asList(1,2,3));
        List<Integer> expected_result = List.of(1,3);
        List<Integer> res = P0515.largestValues(root);

        assertEquals(expected_result, res);
    }
}
