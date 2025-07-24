package Baekjoon.DP;

import java.io.*;

public class Main_1003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] fibonacci = new int[41];
        fibonacci[0] = 0;
        fibonacci[1] = 1;

        for (int i = 2; i <= 40; i++) {
            fibonacci[i] = fibonacci[i-2] + fibonacci[i-1];
        }

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            if (N == 0) {
                sb.append("1 0").append('\n');
            } else {
                sb.append(fibonacci[N-1]).append(' ').append(fibonacci[N]).append('\n');
            }
        }

        System.out.println(sb);
    }
}
