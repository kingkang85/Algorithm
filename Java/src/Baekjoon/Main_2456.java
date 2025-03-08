package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_2456 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[][] scores = new int[3][3];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            scores[0][Integer.parseInt(st.nextToken())-1]++;
            scores[1][Integer.parseInt(st.nextToken())-1]++;
            scores[2][Integer.parseInt(st.nextToken())-1]++;
        }
        br.close();

        int num = 0;  // 결정된 후보
        int maxScore = 0;  // 최고 점수
        boolean found = false;

        for (int i = 0; i < 3; i++) {
            int score = scores[i][0] + 2 * scores[i][1] + 3 * scores[i][2];

            if (score > maxScore) {
                num = i + 1;
                maxScore = score;
                found = true;
            } else if (score == maxScore) {
                if (scores[i][2] > scores[num-1][2]) {
                    num = i + 1;
                } else if (scores[i][2] == scores[num-1][2] && scores[i][1] > scores[num-1][1]) {
                    num = i + 1;
                } else if (scores[i][2] == scores[num-1][2] && scores[i][1] == scores[num-1][1]) {
                    found = false;
                    continue;
                }
                found = true;
            }
        }

        if (!found) {
            System.out.println("0 " + maxScore);
        } else {
            System.out.println(num + " " + maxScore);
        }
    }
}
