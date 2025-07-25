package Baekjoon.TwoPointer;

import java.io.*;
import java.util.*;

public class Main_2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] trees = new int[N];
        int maxHeight = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
            maxHeight = Math.max(maxHeight, trees[i]);
        }

        // 이진 탐색 범위 설정
        int min = 0;          // 절단기 최소 높이
        int max = maxHeight;  // 절단기 최대 높이 (가장 높은 나무까지)
        int result = 0;

        while (min <= max) {
            int mid = (min + max) / 2;

            // mid 높이로 절단했을 때 얻을 수 있는 나무 길이 계산
            long height = 0;
            for (int tree : trees) {
                if (tree - mid > 0) {
                    height += tree - mid;
                }
            }

            if (height >= M) {  // 필요 길이 이상이라면, 더 높은 높이 탐색
                result = mid;
                min = mid + 1;
            } else {
                max = mid - 1;  // 나무가 부족하므로 더 낮은 높이 시도
            }
        }

        System.out.println(result);
    }
}
