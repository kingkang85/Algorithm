package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_9366 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        int[] arr = new int[3];

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            arr[0] = Integer.parseInt(st.nextToken());
            arr[1] = Integer.parseInt(st.nextToken());
            arr[2] = Integer.parseInt(st.nextToken());

            Arrays.sort(arr);

            String result;
            if (arr[0] + arr[1] <= arr[2]) {
                result = "invalid!";
            } else if (arr[0] == arr[1] && arr[1] == arr[2]) {
                result = "equilateral";
            } else if (arr[0] == arr[1] || arr[1] == arr[2] || arr[0] == arr[2]) {
                result = "isosceles";
            } else {
                result = "scalene";
            }

            System.out.println("Case #" + (i+1) + ": " + result);
        }
    }
}
