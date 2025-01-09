// 10811. 바구니 뒤집기
package Baekjoon;

import java.io.*;

public class Main_10811 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = i+1;
        }

        int start, end;
        for (int i = 0; i < M; i++) {
            String[] input2 = br.readLine().split(" ");
            start = Integer.parseInt(input2[0]) - 1;
            end = Integer.parseInt(input2[1]) - 1;

            reverseArray(numbers, start, end);
        }

        for (int i = 0; i < N; i++) {
            System.out.print(numbers[i] + " ");
        }
    }

    public static void reverseArray(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start++;
            end--;
        }
    }
}