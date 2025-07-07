package Baekjoon.Impl;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main_2816 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<String> channels = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            channels.add(br.readLine());
        }

        StringBuilder result = new StringBuilder();
        int arrow = 0;

        // 1. KBS1을 첫 번째로 이동
        int kbs1Pos = channels.indexOf("KBS1");
        while (arrow < kbs1Pos) {
            result.append("1");
            arrow++;
        }
        while (kbs1Pos > 0) {
            Collections.swap(channels, kbs1Pos, kbs1Pos - 1);
            result.append("4");
            kbs1Pos--;
            arrow--;
        }

        // 2. KBS2를 두 번째로 이동
        int kbs2Pos = channels.indexOf("KBS2");
        while (arrow < kbs2Pos) {
            result.append("1");
            arrow++;
        }
        while (kbs2Pos > 1) {
            Collections.swap(channels, kbs2Pos, kbs2Pos - 1);
            result.append("4");
            kbs2Pos--;
            arrow--;
        }

        System.out.println(result);
    }
}
