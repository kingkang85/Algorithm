package Baekjoon.BinarySearch;

import java.io.*;
import java.util.*;

public class Main_2512 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] countries = new int[N];

        int maxMoney = 0, sum = 0;
        for (int i = 0; i < N; i++) {
            int money = Integer.parseInt(st.nextToken());
            maxMoney = Math.max(maxMoney, money);
            sum += money;
            countries[i] = money;
        }

        int totalMoney = Integer.parseInt(br.readLine());

        if (sum <= totalMoney) {
            System.out.println(maxMoney);
        } else {
            int left = 0;
            int right = maxMoney;
            int result = 0;

            while (left <= right) {
                int mid = (left + right) / 2;
                long allocatedSum = 0;

                for (int country : countries) {
                    if (country > mid) {
                        allocatedSum += mid;
                    } else {
                        allocatedSum += country;
                    }
                }

                if (allocatedSum <= totalMoney) {
                    result = mid;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }

            System.out.println(result);
        }
    }
}
