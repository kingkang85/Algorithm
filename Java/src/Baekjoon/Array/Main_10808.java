package Baekjoon.Array;

import java.io.*;

public class Main_10808 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] counts = new int[26];

        for (char str : br.readLine().toCharArray()) {
            counts[str - 'a']++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            sb.append(counts[i]);
            if (i < 25) sb.append(' ');
        }
        System.out.println(sb);
    }
}
