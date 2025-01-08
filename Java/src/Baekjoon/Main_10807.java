package Baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_10807 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] numbers = br.readLine().split(" ");
        String targetNum = br.readLine();

        int result = 0;
        for (String num : numbers) {
            if (num.equals(targetNum)) {
                result += 1;
            }
        }

        System.out.print(result);
    }
}
