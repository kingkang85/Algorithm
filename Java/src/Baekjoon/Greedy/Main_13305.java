package Baekjoon.Greedy;

import java.io.*;
import java.util.*;

public class Main_13305 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] roads = new int[N-1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N-1; i++) {
            roads[i] = Integer.parseInt(st.nextToken());
        }

        int[] price = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            price[i] = Integer.parseInt(st.nextToken());
        }

        long totalPrice = 0;
        int minPrice = price[0];

        for (int i = 0; i < N-1; i++) {
            if (price[i] < minPrice) {
                minPrice = price[i];
            }

            totalPrice += (long) minPrice * roads[i];
        }

        System.out.println(totalPrice);
    }
}
