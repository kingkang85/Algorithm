package Baekjoon.DP;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_2839 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int minCount = -1; // 최소 봉지 수

        // 최대한 5킬로그램 봉지로 배달
        for (int five = n / 5; five >= 0; five--) {
            int remain = n - (five * 5);

            // 3킬로그램 봉지로 배달 가능한 경우
            if (remain % 3 == 0) {
                minCount = five + remain / 3;
                break;
            }
        }
        System.out.println(minCount);
    }
}