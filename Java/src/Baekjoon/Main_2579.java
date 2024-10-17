// 2579. 계단 오르기
package Baekjoon;
import java.io.*;

public class Main_2579 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] scores = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            scores[i] = Integer.parseInt(br.readLine());
        }

        int[] dp = new int[n + 1];
        if (n >= 1) {
            dp[1] = scores[1];
        }
        if (n >= 2) {
            dp[2] = scores[1] + scores[2];
        }

        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i]);
        }
        System.out.println(dp[n]);
    }
}