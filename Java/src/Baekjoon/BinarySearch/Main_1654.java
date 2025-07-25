package Baekjoon.BinarySearch;

import java.io.*;
import java.util.*;

public class Main_1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[] lengths = new int[K];
        int maxLength = 0;
        for (int i = 0; i < K; i++) {
            lengths[i] = Integer.parseInt(br.readLine());
            maxLength = Math.max(maxLength, lengths[i]);
        }

        long min = 1;
        long max = maxLength;
        long result = 0;

        while (min <= max) {
            long mid = (min + max) / 2;

            long count = 0;
            for (int length : lengths) {
                count += length / mid;
            }

            if (count >= N) {
                result = mid;
                min = mid + 1;
            } else {
                max = mid - 1;
            }
        }

        System.out.println(result);
    }
}
