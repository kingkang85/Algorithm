package Baekjoon.TwoPointer;

import java.io.*;
import java.util.*;

/**
 * 10025. 게으른 백곰
 *
 * 1. 배열에 얼음 정보 저장
 * 2. 좌우로 K만큼 떨어진 슬라이딩 윈도우를 유지하며 얼음들의 합 구하기
 */
public class Main_10025 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] ice = new int[1000001];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int g = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            ice[x] = g;
        }

        int start = 0;
        int end = Math.min(2 * K, 1000000);
        int maxValue = 0;
        for (int i = start; i <= end; i++) {
            maxValue += ice[i];
        }

        int currentSum = maxValue;
        while (end < 1000000) {
            currentSum -= ice[start];
            start++;

            end++;
            currentSum += ice[end];

            if (currentSum > maxValue) {
                maxValue = currentSum;
            }
        }

        System.out.println(maxValue);
    }
}
