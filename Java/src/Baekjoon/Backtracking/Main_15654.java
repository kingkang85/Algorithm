package Baekjoon.Backtracking;

import java.io.*;
import java.util.*;

public class Main_15654 {
    static int N, M;
    static int[] seq;
    static boolean[] visited;
    static int[] result;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        seq = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) seq[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(seq);

        visited = new boolean[N];
        result = new int[M];

        perm(0);
        System.out.println(sb);
    }

    static void perm(int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(result[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                result[depth] = seq[i];
                perm(depth + 1);
                visited[i] = false;
            }
        }
    }
}
