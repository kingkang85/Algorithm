package Baekjoon.Impl;

import java.io.*;

public class Main_2292 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        if (N == 1) {
            System.out.println(1);
            return;
        }

        int layer = 1;
        int maxRoom = 1;

        while (maxRoom < N) {
            maxRoom += 6 * layer;
            layer++;
        }

        System.out.println(layer);
    }
}
