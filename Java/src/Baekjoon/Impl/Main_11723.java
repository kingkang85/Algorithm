package Baekjoon.Impl;

import java.io.*;

public class Main_11723 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int S = 0;

        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            String[] input = br.readLine().split(" ");
            String operation = input[0];
            int num = (input.length == 2) ? Integer.parseInt(input[1]) : 0;

            if (operation.equals("add")) {
                S |= (1 << (num - 1));
            } else if (operation.equals("remove")) {
                S &= ~(1 << (num - 1));
            } else if (operation.equals("check")) {
                sb.append((S & (1 << (num - 1))) != 0 ? "1\n" : "0\n");
            } else if (operation.equals("toggle")) {
                S ^= (1 << (num - 1));
            } else if (operation.equals("all")) {
                S = (1 << 20) - 1;
            } else if (operation.equals("empty")) {
                S = 0;
            }
        }

        System.out.println(sb);
    }
}
