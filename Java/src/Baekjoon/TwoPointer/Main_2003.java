package Baekjoon.TwoPointer;

import java.io.*;
import java.util.*;

public class Main_2003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] seq = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }

        int count = 0, left = 0, sum = 0;

        for (int right = 0; right < N; right++) {
            sum += seq[right];

            while (sum > M && left <= right) {
                sum -= seq[left];
                left++;
            }

            if (sum == M) {
                count++;
            }
        }

        System.out.println(count);
    }
}
