// 2439. 별 찍기 - 2
package Baekjoon;

import java.io.*;

public class Main_2439 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();  // 문자열 처리 클래스

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            sb.append(" ".repeat(N-i-1))
                    .append("*".repeat(i+1))
                    .append("\n");
        }
        System.out.print(sb);
    }
}