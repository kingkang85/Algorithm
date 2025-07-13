package Baekjoon.Backtracking;

import java.io.*;
import java.util.*;

public class Main_15650 {
    static int N, M;
    static int[] result;
    static BufferedWriter bw;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        result = new int[M];
        comb(0, 1);

        br.close();
        bw.close();
    }

    static void comb(int depth, int start) throws IOException {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                bw.write(String.valueOf(result[i]));
                if (i < M - 1) bw.write(" ");
            }
            bw.newLine();
            return;
        }

        for (int i = start; i <= N; i++) {
            result[depth] = i;
            comb(depth + 1, i + 1);
        }
    }
}
