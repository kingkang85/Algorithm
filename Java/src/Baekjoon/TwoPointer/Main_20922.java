package Baekjoon.TwoPointer;

import java.io.*;
import java.util.*;

public class Main_20922 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] seq = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }

        int[] counts = new int[100001];
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < N; right++) {
            counts[seq[right]]++;

            while (counts[seq[right]] > K) {
                counts[seq[left]]--;
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }

        System.out.println(maxLength);
    }
}
