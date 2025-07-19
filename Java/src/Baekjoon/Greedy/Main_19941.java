package Baekjoon.Greedy;

import java.io.*;
import java.util.*;

/**
 * 19941. 햄버거 분배
 *
 * 그리디 알고리즘 (매 순간 최선의 선택!)
 * 1. 각 사람은 자신의 위치에서 거리 K 이내의 햄버거 중
 *    가장 왼쪽에 있는 햄버거 선택
 * 2. 선택된 햄버거 표시
 * 3. 햄버거 먹은 사람 카운트
 */
public class Main_19941 {
    static int N, K;
    static String[] positions;
    static boolean[] eaten;
    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        eaten = new boolean[N];

        positions = br.readLine().split("");

        for (int i = 0; i < N; i++) {
            if (positions[i].equals("P")) {
                eatHamburger(i);
            }
        }

        System.out.println(count);
    }

    static void eatHamburger(int index) {
        for (int i = index - K; i <= index + K; i++) {
            if (i >= 0 && i < N && !eaten[i] && positions[i].equals("H")) {
                eaten[i] = true;
                count++;
                return;
            }
        }
    }
}
