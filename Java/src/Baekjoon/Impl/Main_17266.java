package Baekjoon.Impl;

import java.io.*;
import java.util.StringTokenizer;

public class Main_17266 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int lamps[] = new int[M];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            lamps[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = N;
        int result = N;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (canLightAll(lamps, N, mid)) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(result);
    }

    private static boolean canLightAll(int[] lamps, int N, int height) {
        if (lamps[0] > height) return false;

        for (int i = 0; i < lamps.length - 1; i++) {
            int gap = lamps[i+1] - lamps[i];
            if (gap > 2 * height) return false;
        }

        if (N - lamps[lamps.length - 1] > height) return false;

        return true;
    }
}
