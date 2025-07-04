package Baekjoon.String;

import java.io.*;
import java.util.HashSet;

public class Main_1235 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        String[] students = new String[N];
        for (int i = 0; i < N; i++) {
            students[i] = br.readLine();
        }

        int len = students[0].length();

        for (int k = 1; k <= len; k++) {
            HashSet<String> set = new HashSet<>();

            for (int i = 0; i < N; i++) {
                String tail = students[i].substring(len - k);
                set.add(tail);
            }

            if (set.size() == N) {
                System.out.println(k);
                return;
            }
        }
    }
}
