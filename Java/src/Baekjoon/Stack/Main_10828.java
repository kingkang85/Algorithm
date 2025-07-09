package Baekjoon.Stack;

import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main_10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Integer> stack = new ArrayDeque<>();

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            String operation = input[0];

            switch (operation) {
                case "push" -> stack.push(Integer.parseInt(input[1]));
                case "pop" -> bw.write((stack.isEmpty() ? -1 : stack.pop()) + "\n");
                case "size" -> bw.write(stack.size() + "\n");
                case "empty" -> bw.write((stack.isEmpty() ? 1 : 0) + "\n");
                case "top" -> bw.write((stack.isEmpty() ? -1 : stack.peek()) + "\n");
            }
        }

        bw.flush();
    }
}
