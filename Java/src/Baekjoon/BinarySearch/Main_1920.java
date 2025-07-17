package Baekjoon.BinarySearch;

import java.io.*;
import java.util.*;


public class Main_1920 {
    static int[] numbers;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());

        numbers = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) numbers[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(numbers);

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            if (hasNumber(Integer.parseInt(st.nextToken()))) {
                sb.append(1).append('\n');
            } else {
                sb.append(0).append('\n');
            }
        }

        System.out.println(sb);
    }

    static boolean hasNumber(int number) {
        int left = 0;
        int right = numbers.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (numbers[mid] == number) {
                return true;
            } else if (numbers[mid] < number) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }
}
