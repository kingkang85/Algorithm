package Baekjoon.TwoPointer;

import java.io.*;
import java.util.*;

public class Main_21921 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] visitors = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            visitors[i] = Integer.parseInt(st.nextToken());
        }

        // 슬라이딩 윈도우 초기화
        int sum = 0;
        for (int i = 0; i < K; i++) {
            sum += visitors[i];
        }

        int max = sum, count = 1, start = 0;
        for (int i = K; i < N; i++) {
            sum -= visitors[start++];
            sum += visitors[i];

            if (sum > max) {
                max = sum;
                count = 1;
            } else if (sum == max) {
                count++;
            }
        }

        if (max == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(max);
            System.out.println(count);
        }
    }
}
