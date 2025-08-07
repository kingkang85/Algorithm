package Baekjoon.Backtracking;

import java.io.*;
import java.util.*;

public class Main_15666 {
    static int N, M;
    static int[] seq, result;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        seq = new int[N];
        for (int i = 0; i < N; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(seq);

        result = new int[M];
        backtrack(0, 0);
        System.out.println(sb);
    }

    static void backtrack(int depth, int start) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(result[i]);
                if (i < M - 1) sb.append(' ');
            }

            sb.append('\n');
            return;
        }

        int prev = -1;

        for (int i = start; i < N; i++) {
            if (prev == seq[i]) continue;

            result[depth] = seq[i];
            prev = seq[i];

            backtrack(depth+1, i);
        }
    }
}
