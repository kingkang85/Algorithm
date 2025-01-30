package Baekjoon.Bruteforce;

import java.io.*;
import java.util.*;

public class Main_2503 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        boolean[] check = new boolean[988];

        for (int i = 123; i <= 987; i++) {
            String num = String.valueOf(i);

            if (num.charAt(0) == '0' || num.charAt(1) == '0' || num.charAt(2) == '0') continue;
            if (num.charAt(0) == num.charAt(1) || num.charAt(1) == num.charAt(2) || num.charAt(0) == num.charAt(2)) continue;

            check[i] = true;
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            String guess = st.nextToken();
            int s = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            for (int j = 123; j <= 987; j++) {
                if (check[j]) {
                    String ans = String.valueOf(j);  // 정답 가능성이 있는 수
                    int ns = 0;
                    int nb = 0;
                    for (int k = 0; k < 3; k++) {
                        char splitedGuess = guess.charAt(k);
                        for (int l = 0; l < 3; l++) {
                            char splitedAns = ans.charAt(l);

                            if (splitedGuess == splitedAns && k == l) ns++;
                            else if (splitedGuess == splitedAns && k != l) nb++;
                        }
                    }

                    if (ns != s || nb != b) check[j] = false;
                }
            }
        }

        int result = 0;
        for (int i = 123; i <= 987; i++) {
            if (check[i]) result++;
        }

        System.out.println(result);
    }
}
