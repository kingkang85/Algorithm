package Baekjoon.Impl;

import java.io.*;

public class Main_2742 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = N; i >= 1; i--) {
            System.out.println(i);
        }
    }
}
