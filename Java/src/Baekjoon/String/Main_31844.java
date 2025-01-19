package Baekjoon.String;

import java.io.*;

public class Main_31844 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String stock = br.readLine();

        int robot = stock.indexOf('@');
        int box = stock.indexOf('#');
        int target = stock.indexOf('!');

        if ((box < robot && box < target) || (box > robot && box > target)) {
            System.out.println(-1);
        } else {
            System.out.println(Math.abs(target - robot) - 1);
        }
    }
}
