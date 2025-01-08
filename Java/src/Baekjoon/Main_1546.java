package Baekjoon;

import java.io.*;

public class Main_1546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] scores = br.readLine().split(" ");

        int maxScore = 0;
        for (String score : scores) {
            if (Integer.parseInt(score) > maxScore) {
                maxScore = Integer.parseInt(score);
            }
        }

        double sumScore = 0;
        for (String score : scores) {
            sumScore += (Double.parseDouble(score) / maxScore * 100);
        }

        System.out.print(sumScore / N);
    }
}
