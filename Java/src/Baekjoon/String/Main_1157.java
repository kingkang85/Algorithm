package Baekjoon.String;

import java.io.*;

public class Main_1157 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().toUpperCase();

        int[] counts = new int[26];

        for (char c : input.toCharArray()) {
            counts[c - 'A']++;
        }

        int maxValue = -1;
        char answer = '?';

        for (int i = 0; i < 26; i++) {
            if (counts[i] > maxValue) {
                maxValue = counts[i];
                answer = (char)('A' + i);
            } else if (counts[i] == maxValue) {
                answer = '?';
            }
        }

        System.out.println(answer);
    }
}
