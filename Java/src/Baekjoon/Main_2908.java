package Baekjoon;

import java.io.*;
import java.util.StringTokenizer;

public class Main_2908 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = reverse(st.nextToken());
        int B = reverse(st.nextToken());

        System.out.println(Math.max(A, B));
    }

    public static int reverse(String str) {
        return (str.charAt(2) - '0') * 100 +
                (str.charAt(1) - '0') * 10 +
                (str.charAt(0) - '0');
    }
}
