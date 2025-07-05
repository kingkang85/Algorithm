package Baekjoon.String;

import java.io.*;

public class Main_1343 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String board = br.readLine();
        StringBuilder sb = new StringBuilder();
        int count = 0;

        for (char c : board.toCharArray()) {
            if (c == 'X') {
                count++;
            } else {
                if (count % 2 != 0) {
                    System.out.println(-1);
                    return;
                }

                sb.append("AAAA".repeat(count / 4));
                count %= 4;

                sb.append("BB".repeat(count / 2));
                count = 0;

                sb.append('.');
            }
        }

        if (count % 2 != 0) {
            System.out.println(-1);
            return;
        }
        sb.append("AAAA".repeat(count / 4));
        count %= 4;
        sb.append("BB".repeat(count / 2));

        System.out.println(sb);
    }
}
