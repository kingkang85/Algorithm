package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_2960 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        int[] nums = new int[N+1];
        int count = 0;
        boolean found = false;

        for (int i = 2; i <= N; i++) {
            nums[i] = i;
        }

        for (int i = 2; i <= N; i++) {
            if (nums[i] == 0) continue;

            for (int j = i; j <= N; j+=i) {
                if (nums[j] != 0) {
                    nums[j] = 0;
                    count++;
                }

                if (count == K) {
                    System.out.println(j);
                    found = true;
                    break;
                }
            }

            if (found) break;
        }
    }
}
