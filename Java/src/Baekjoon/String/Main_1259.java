package Baekjoon.String;

import java.io.*;

public class Main_1259 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String input = br.readLine();

            if (input.equals("0")) break;

            boolean found = false;
            for (int i = 0; i < input.length() / 2; i++) {
                if (input.charAt(i) != input.charAt(input.length() - 1 - i)) {
                    found = true;
                    break;
                }
            }

            if (found) System.out.println("no");
            else System.out.println("yes");
        }
    }
}