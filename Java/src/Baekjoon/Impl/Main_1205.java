package Baekjoon.Impl;

import java.io.*;
import java.util.StringTokenizer;

public class Main_1205 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int newScore = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int[] scores = new int[N];
        if (N > 0) {
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                scores[i] = Integer.parseInt(st.nextToken());
            }
        }

        int rank = 1;
        for (int i = 0; i < N; i++) {
            if (scores[i] > newScore) {
                rank++;
            } else {
                break;
            }
        }

        if (N == P && scores[N - 1] >= newScore) {
            System.out.println(-1);
        } else {
            System.out.println(rank);
        }
    }
}
