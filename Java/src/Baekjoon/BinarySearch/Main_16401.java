package Baekjoon.BinarySearch;

import java.io.*;
import java.util.*;

public class Main_16401 {
    static int[] snacks;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        snacks = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            snacks[i] = Integer.parseInt(st.nextToken());
        }

        // 이분 탐색으로 최대 길이 찾기
        int left = 1;
        int right = Arrays.stream(snacks).max().getAsInt();
        int maxLength = 0;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (canDivide(mid)) {
                maxLength = mid;
                left = mid + 1;  // 더 긴 길이 탐색
            } else {
                right = mid - 1;  // 더 짧은 길이 탐색
            }
        }

        System.out.println(maxLength);
    }

    static boolean canDivide(int length) {
        int count = 0;
        for (int snack : snacks) {
            count += snack / length;
        }

        return count >= M;
    }
}
