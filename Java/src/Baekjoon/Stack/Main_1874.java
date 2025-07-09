package Baekjoon.Stack;

import java.io.*;
import java.util.*;

public class Main_1874 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Deque<Integer> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

        int current = 1;
        boolean possible = true;

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());

            while (current <= num) {
                stack.push(current++);
                sb.append("+\n");
            }

            if (stack.peek() == num) {
                stack.pop();
                sb.append("-\n");
            } else {
                possible = false;
                break;
            }
        }

        if (possible) {
            System.out.println(sb);
        } else {
            System.out.println("NO");
        }
    }
}
