package Baekjoon.Impl;

import java.io.*;
import java.util.*;

/**
 * 10431. 줄세우기
 *
 * 학생이 한 명씩 들어온다고 할 때,
 * 앞에 있는 학생들 중 자신보다 키가 큰 학생들의 수를 세면 됨
 */
public class Main_10431 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int P = Integer.parseInt(br.readLine());

        for (int i = 0; i < P; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int T = Integer.parseInt(st.nextToken());

            int[] students = new int[20];
            for (int j = 0; j < 20; j++) {
                students[j] = Integer.parseInt(st.nextToken());
            }

            int totalSteps = 0;
            for (int k = 0; k < 20; k++) {
                for (int l = 0; l < k; l++) {
                    if (students[k] < students[l]) {
                        totalSteps++;
                    }
                }
            }

            System.out.println(T + " " + totalSteps);
        }
    }
}

