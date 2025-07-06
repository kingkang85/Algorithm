package Baekjoon.Impl;

import java.io.*;
import java.util.StringTokenizer;

public class Main_23971 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int result = ((H+N) / (N+1)) * ((W+M) / (M+1));
        System.out.println(result);
    }
}
