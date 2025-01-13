package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_31831 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int count = 0;
        int stress = 0;

        for (int i = 0; i < N; i++) {
            int change = Integer.parseInt(st.nextToken());

            stress += change;

            if(stress < 0) {
                stress = 0;
            }

            if(stress >= M) {
                count++;
            }
        }

        System.out.print(count);
    }
}
