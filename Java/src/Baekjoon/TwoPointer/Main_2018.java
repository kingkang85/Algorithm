package Baekjoon.TwoPointer;

import java.io.*;

public class Main_2018 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int count = 0;
        int start = 1;
        int sum = 0;

        for (int end = 1; end <= N ; end++) {
            sum += end;

            while (sum > N && start <= end) {
                sum -= start;
                start++;
            }

            if (sum == N) {
                count++;
            }
        }

        System.out.println(count);
    }
}
