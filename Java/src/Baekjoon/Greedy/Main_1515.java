package Baekjoon.Greedy;

import java.io.*;

public class Main_1515 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int n = 1;
        int pointer = 0;

        while (pointer < input.length()) {
            String currentNumber = String.valueOf(n);
            for (int i = 0; i < currentNumber.length(); i++) {
                if (pointer < input.length() && currentNumber.charAt(i) == input.charAt(pointer)) {
                    pointer++;
                }
            }
            n++;
        }

        System.out.println(n-1);
    }
}
