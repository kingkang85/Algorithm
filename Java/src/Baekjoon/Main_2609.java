// 2609. 최대공약수와 최소공배수
package Baekjoon;

import java.io.*;

public class Main_2609 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        int gcd = getGCD(N, M);
        System.out.println(gcd);
        System.out.println(N * M / gcd);
    }

    public static int getGCD(int num1, int num2) {
        if (num1 % num2 == 0) {
            return num2;
        }
        return getGCD(num2, num1%num2);
    }
}
