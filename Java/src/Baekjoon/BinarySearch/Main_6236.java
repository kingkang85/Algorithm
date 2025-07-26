package Baekjoon.BinarySearch;

import java.io.*;
import java.util.*;

public class Main_6236 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] money = new int[N];
        int min = 0;  // 하루 최대 돈
        int max = 0;  // N일치 돈의 합
        for (int i = 0; i < N; i++) {
            money[i] = Integer.parseInt(br.readLine());
            min = Math.max(min, money[i]);
            max += money[i];
        }

        int result = 0;
        while (min <= max) {
            int mid = (min + max) / 2;
            int count = 1;     // 인출한 횟수
            int remain = mid;  // 쓰고 남은 돈

            for (int m : money) {
                if (m > remain) {
                    count++;
                    remain = mid - m;
                } else {
                    remain -= m;
                }
            }

            // M번 이하더라도 억지로 인출하여 M번 맞출 수 있음
            if (count <= M) {
                result = mid;
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }

        System.out.println(result);
    }
}
