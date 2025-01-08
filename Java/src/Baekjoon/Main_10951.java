// 10951. A+B - 4
package Baekjoon;

import java.io.*;

public class Main_10951 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;

        while ((str = br.readLine()) != null) {
            String[] input = str.split(" ");
            System.out.println(Integer.parseInt(input[0]) + Integer.parseInt(input[1]));
        }
    }
}