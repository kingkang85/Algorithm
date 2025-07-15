package Baekjoon.Impl;

import java.io.*;

/**
 * 4659. 비밀번호 발음하기
 *
 * 1. 모음(a,e,i,o,u) 중 하나라도 존재하는지 check
 * 2. 연속한 자음과 모음 개수가 3개인지 check
 * 3. (ee, oo 제외) 같은 글자가 연속하는지 check
 */
public class Main_4659 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String password = br.readLine();

            if (password.equals("end")) break;

            boolean hasVowel = false;  // 모음이 존재하는지
            int vowelCount = 0, consonantCount = 0;  // 연속한 자음과 모음 개수
            boolean isAcceptable = true;  // 결과

            for (int i = 0; i < password.length(); i++) {
                char c = password.charAt(i);

                if (isVowel(c)) {
                    hasVowel = true;
                    vowelCount++;
                    consonantCount = 0;
                } else {
                    consonantCount++;
                    vowelCount = 0;
                }

                // 연속한 자음이나 모음 개수가 3개라면 false
                if (vowelCount == 3 || consonantCount == 3) {
                    isAcceptable = false;
                    break;
                }

                // 같은 글자가 연속한다면 false
                if (i > 0 && c != 'e' && c != 'o' && c == password.charAt(i-1)) {
                    isAcceptable = false;
                    break;
                }
            }

            // 모음이 존재하지 않으면 false
            if (!hasVowel) isAcceptable = false;

            System.out.println("<" + password + "> is " + (isAcceptable ? "acceptable." : "not acceptable."));
        }
    }

    // 모음 확인 함수
    static boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
