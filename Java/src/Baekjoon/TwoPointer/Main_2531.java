package Baekjoon.TwoPointer;

import java.io.*;
import java.util.*;

public class Main_2531 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] plates = new int[N];
        for (int i = 0; i < N; i++) {
            plates[i] = Integer.parseInt(br.readLine());
        }

        int[] counts = new int[d+1];
        int uniqueCount = 0;

        // 첫 번째 윈도우 초기화
        for (int i = 0; i < k; i++) {
            int sushi = plates[i];

            if (counts[sushi] == 0) {
                uniqueCount++;
            }

            counts[sushi]++;
        }

        // 첫 번째 윈도우의 최대값 초기화
        int maxCount = counts[c] == 0 ? uniqueCount + 1 : uniqueCount;

        // 슬라이딩 윈도우
        for (int i = 1; i < N; i++) {
            int removeSushi = plates[(i - 1) % N];
            counts[removeSushi]--;
            if (counts[removeSushi] == 0) {
                uniqueCount--;
            }

            int addSushi = plates[(i + k - 1) % N];
            if (counts[addSushi] == 0) {
                uniqueCount++;
            }
            counts[addSushi]++;

            int currentCount = counts[c] == 0 ? uniqueCount + 1 : uniqueCount;

            if (currentCount > maxCount) {
                maxCount = currentCount;
            }
        }

        System.out.println(maxCount);
    }
}
