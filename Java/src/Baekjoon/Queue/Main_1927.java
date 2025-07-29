package Baekjoon.Queue;

import java.io.*;
import java.util.*;

public class Main_1927 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(br.readLine());

            if (x != 0) {
                pq.offer(x);
            } else {
                sb.append((!pq.isEmpty()) ? pq.poll() : 0).append('\n');
            }
        }

        System.out.println(sb);
    }
}
