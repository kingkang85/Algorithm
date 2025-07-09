package Baekjoon.Stack;

import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main_2493 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] tops = br.readLine().split(" ");

        int[] result = new int[N];
        Deque<int[]> stack = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            int height = Integer.parseInt(tops[i]);

            while (!stack.isEmpty() && stack.peek()[1] < height) {
                stack.pop();
            }

            if (stack.isEmpty()) {
                result[i] = 0;
            } else {
                result[i] = stack.peek()[0];
            }

            stack.push(new int[]{i + 1, height});
        }

        StringBuilder sb = new StringBuilder();
        for (int num : result) {
            sb.append(num).append(' ');
        }
        System.out.println(sb.toString().trim());
    }
}
