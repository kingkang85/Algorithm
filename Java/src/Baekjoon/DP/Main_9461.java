package Baekjoon.DP;

import java.io.*;

public class Main_9461 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        long[] triangles = new long[101];
        triangles[0] = 0;
        triangles[1] = 1;
        triangles[2] = 1;
        triangles[3] = 1;
        triangles[4] = 2;

        for (int i = 5; i <= 100; i++) {
            triangles[i] = triangles[i-5] + triangles[i-1];
        }

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            sb.append(triangles[N]).append('\n');
        }

        System.out.println(sb);
    }
}
