package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_10250 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int H = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            int floor = N % H == 0 ? H : N % H;
            int roomNo = N % H == 0 ? N / H : N / H + 1;

            if (roomNo < 10) {
                sb.append(floor).append("0").append(roomNo);
            } else {
                sb.append(floor).append(roomNo);
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}
