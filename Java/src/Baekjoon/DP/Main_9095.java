package Baekjoon.DP;
import java.io.*;

public class Main_9095 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());
        for (int i = 0; i < tc; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] dp = new int[11];
            dp[0] = 1;
            dp[1] = 2;
            dp[2] = 4;

            for (int j = 3; j < 11; j++) {
                dp[j] = dp[j-3] + dp[j-2] + dp[j-1];
            }
            System.out.println(dp[n-1]);
        }
    }
}