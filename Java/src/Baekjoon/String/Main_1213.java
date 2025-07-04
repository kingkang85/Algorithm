package Baekjoon.String;

import java.io.*;

public class Main_1213 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int[] count = new int[26];

        // 각 문자 개수 세기
        for (char c : str.toCharArray()) {
            count[c - 'A']++;
        }

        // 홀수 개인 문자 개수 확인
        int oddCount = 0;
        char oddChar = 0;
        for (int i = 0; i < 26; i++) {
            if (count[i] % 2 == 1) {
                oddCount++;
                oddChar = (char)('A' + i);
            }
        }

        // 팰린드롬 불가능
        if (oddCount > 1) {
            System.out.println("I'm Sorry Hansoo");
            return;
        }

        StringBuilder front = new StringBuilder();

        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < count[i] / 2; j++) {
                front.append((char)('A' + i));
            }
        }

        StringBuilder result = new StringBuilder(front);
        if (oddCount == 1) {
            result.append(oddChar);
        }
        result.append(front.reverse());

        System.out.println(result);
    }
}
