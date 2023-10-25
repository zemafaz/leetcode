package leetcode;

import java.util.Arrays;
import java.util.PriorityQueue;

public class P1631 {

    private static class Args {
        public int[][] heights;
        public int output;

        public Args(int[][] heights, int output) {
            this.heights = heights;
            this.output = output;
        }

        @Override
        public String toString() {
            return String.format("{heights: %s, output: %d}",
                    Arrays.deepToString(this.heights),
                    this.output);
        }
    }

    private static int minimumEffortPath(int[][] heights) {
        int rows = heights.length, cols = heights[0].length;
        int[][] dist = new int[rows][cols];
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a,b) -> Integer.compare(a[0], b[0]));
        minHeap.add(new int[]{0,0,0});

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
        }

        dist[0][0] = 0;

        int[][] directions = {{0,1}, {1,0}, {-1, 0}, {0, -1}};

        while (!minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int effort = top[0], x = top[1], y=top[2];

            if (effort > dist[x][y]) continue;

            if (x == rows - 1 && y == cols - 1) return effort;

            for (int[] dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                    int new_effort = Math.max(effort, Math.abs(heights[x][y] - heights[nx][ny]));
                    if (new_effort < dist[nx][ny]) {
                        dist[nx][ny] = new_effort;
                        minHeap.add(new int[]{new_effort, nx, ny});
                    }
                }
            }

        }
        return -1;
    }

    public static void main(String[] args) {
        Args[] testArgs = new Args[3];
        int[][] heights1 = {{1,2,2},{3,8,2},{5,3,5}};
        testArgs[0] = new Args(heights1, 2);
        int[][] heights2 = {{1,2,3},{3,8,4},{5,3,5}};
        testArgs[1] = new Args(heights2, 1);
        int[][] heights3 = {{1,2,1,1,1},{1,2,1,2,1},{1,2,1,2,1},{1,2,1,2,1},{1,1,1,2,1}};
        testArgs[2] = new Args(heights3, 0);

        boolean failed = false;
        for (int i = 0; i < testArgs.length; i++) {
            Args test = testArgs[i];
            int res = minimumEffortPath(test.heights);
            if (res != test.output) {
                System.out.println(String.format("Failed test %d: expected %d, returned %d", i + 1, test.output, res));
                failed = true;
            }
        }

        if (!failed) {
            System.out.println("Passed all tests!");
        }
    }

}
