package Baekjoon.Impl;

import java.io.*;

public class Main_1652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        char[][] room = new char[N][N];

        for (int i = 0; i < N; i++) {
            room[i] = br.readLine().toCharArray();
        }

        int row = 0;
        int col = 0;

        for (int i = 0; i < N; i++) {
            int cnt = 0;
            for (int j = 0; j < N; j++) {
                if (room[i][j] == '.') {
                    cnt++;
                } else {
                    if (cnt >= 2) {
                        row++;
                    }
                    cnt = 0;
                }
            }
            if (cnt >= 2) {
                row++;
            }
        }

        for (int i = 0; i < N; i++) {
            int cnt = 0;
            for (int j = 0; j < N; j++) {
                if (room[j][i] == '.') {
                    cnt++;
                } else {
                    if (cnt >= 2) {
                        col++;
                    }
                    cnt = 0;
                }
            }
            if (cnt >= 2) {
                col++;
            }
        }

        System.out.println(row + " " + col);
    }
}
