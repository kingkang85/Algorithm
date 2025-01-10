package Baekjoon;

import java.io.*;

public class Main_1152 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().trim();

        if (input.isEmpty()) {
            System.out.print(0);
        } else {
            System.out.print(input.split(" ").length);
        }
    }
}
