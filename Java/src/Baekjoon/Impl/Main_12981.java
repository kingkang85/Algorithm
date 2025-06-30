package Baekjoon.Impl;

import java.io.*;

public class Main_12981 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int R = Integer.parseInt(input[0]);
        int G = Integer.parseInt(input[1]);
        int B = Integer.parseInt(input[2]);

        // 서로 다른 색 3개씩 포장
        int result = Math.min(Math.min(R, G), B);
        R -= result;
        G -= result;
        B -= result;

        // 같은 색 3개씩 포장
        result += (R / 3) + (G / 3) + (B / 3);
        R %= 3;
        G %= 3;
        B %= 3;

        // 남은 공들로 2개씩 포장
        int remain = R + G + B;
        result += remain / 2;

        // 남은 1개 포장
        result += (remain % 2);

        System.out.println(result);
    }
}
