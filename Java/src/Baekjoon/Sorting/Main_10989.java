package Baekjoon.Sorting;

import java.io.*;

public class Main_10989 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] cnts = new int[10001];

        for (int i = 0; i < N; i++) {
            cnts[Integer.parseInt(br.readLine())] += 1;
        }
        br.close();

        for (int i = 0; i < 10001; i++) {
            while (cnts[i] > 0) {
                sb.append(i).append('\n');
                cnts[i] -= 1;
            }
        }

        System.out.println(sb);
    }
}
