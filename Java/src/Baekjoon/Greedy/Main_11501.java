package Baekjoon.Greedy;

import java.io.*;
import java.util.*;

public class Main_11501 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());

            int[] price = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                price[i] = Integer.parseInt(st.nextToken());
            }

            long totalProfit = 0;
            int maxPrice = 0;

            for (int i = N - 1; i >= 0; i--) {
                if (price[i] > maxPrice) {
                    maxPrice = price[i];
                } else {
                    totalProfit += (maxPrice - price[i]);
                }
            }

            System.out.println(totalProfit);
        }
    }
}
