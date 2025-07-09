package Baekjoon.Queue;

import java.io.*;
import java.util.*;

public class Main_10845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        Deque<Integer> queue = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            String operation = input[0];

            switch (operation) {
                case "push" -> queue.offer(Integer.parseInt(input[1]));
                case "pop" -> bw.write((queue.isEmpty() ? -1 : queue.poll()) + "\n");
                case "size" -> bw.write(queue.size() + "\n");
                case "empty" -> bw.write((queue.isEmpty() ? 1 : 0) + "\n");
                case "front" -> bw.write((queue.isEmpty() ? -1 : queue.peek()) + "\n");
                case "back" -> bw.write((queue.isEmpty() ? -1 : queue.peekLast()) + "\n");
            }
        }

        bw.flush();
    }
}
