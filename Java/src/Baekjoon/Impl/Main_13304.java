package Baekjoon.Impl;

import java.io.*;
import java.util.*;

public class Main_13304 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] student = new int[5];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int sex = Integer.parseInt(st.nextToken());
            int year = Integer.parseInt(st.nextToken());

            if (year == 1 || year == 2) {
                student[0] += 1;
            } else if (sex == 0 && (year == 3 || year == 4)) {
                student[1] += 1;
            } else if (sex == 1 && (year == 3 || year == 4)) {
                student[2] += 1;
            } else if (sex == 0 && (year == 5 || year == 6)) {
                student[3] += 1;
            } else {
                student[4] += 1;
            }
        }

        int room = 0;
        for (int i = 0; i < 5; i++) {
            room += (int)Math.ceil((double)student[i] / K);
        }

        System.out.println(room);
    }
}
