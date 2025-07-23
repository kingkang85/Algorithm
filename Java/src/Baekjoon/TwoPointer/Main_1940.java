package Baekjoon.TwoPointer;

import java.io.*;
import java.util.*;

/**
 * 1940. 주몽
 *
 * 1. 재료를 저장 후 정렬
 * 2. 시작과 끝의 합을 구한 후,
 *    필요한 수보다 작으면 시작 + 1
 *    필요한 수보다 크면 끝 - 1
 */
public class Main_1940 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        int[] ingredients = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            ingredients[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(ingredients);

        int start = 0;
        int end = N - 1;
        int result = 0;

        while (start < end) {
            int sum = ingredients[start] + ingredients[end];

            if (sum == M) {
                result++;
                start++;
                end--;
            } else if (sum < M) {
                start++;
            } else {
                end--;
            }
        }

        System.out.println(result);
    }
}
