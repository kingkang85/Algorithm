package Baekjoon.DP;

import java.io.*;
import java.util.*;

public class Main_12865 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] weight = new int[N+1];
        int[] value = new int[N+1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            weight[i] = Integer.parseInt(st.nextToken());
            value[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[K+1];

        for (int i = 1; i <= N; i++) {
            for (int w = K; w >= weight[i]; w--) {
                dp[w] = Math.max(dp[w], dp[w - weight[i]] + value[i]);
            }
        }

        System.out.println(dp[K]);
    }
}
