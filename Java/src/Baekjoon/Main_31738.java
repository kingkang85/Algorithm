package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_31738 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long N = Long.parseLong(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        long result = 1;
        for (int i = 1; i <= Math.min(N, M); i++) {
            result = (result * i) % M;
            if (result == 0) break;
        }

        System.out.print(result);
    }
}
