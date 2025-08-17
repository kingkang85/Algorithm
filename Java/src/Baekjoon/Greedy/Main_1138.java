package Baekjoon.Greedy;

import java.io.*;
import java.util.*;

public class Main_1138 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] line = new int[N];
        for (int i = 0; i < N; i++) {
            int memory = Integer.parseInt(st.nextToken());

            int count = 0;  // 빈 공간의 개수
            for (int j = 0; j < N; j++) {
                if (line[j] == 0) {
                    count++;
                }

                // 빈 공간이 기억 정보와 같아지고 현재 자리가 비어있으면
                if (count == memory + 1&& line[j] == 0) {
                    line[j] = i + 1;
                    break;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int people : line) {
            sb.append(people).append(' ');
        }

        System.out.println(sb.toString().trim());
    }
}
