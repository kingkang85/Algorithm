package Baekjoon.DP;

import java.io.*;

public class Main_9655 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // dp[i]: i개가 남았을 때 현재 턴인 사람이 이길 수 있는가?
        boolean[] dp = new boolean[1001];

        dp[1] = true;
        dp[2] = false;
        dp[3] = true;

        for (int i = 4; i <= N; i++) {
            // 1개 가져가서 상대가 (i-1)개 상황
            // 3개 가져가서 상대가 (i-3)개 상황
            // 둘 중 하나라도 상대가 지는 상황이라면 무조건 내가 이김
            dp[i] = !dp[i-1] || !dp[i-3];
        }

        System.out.println(dp[N] ? "SK" : "CY");
    }
}
