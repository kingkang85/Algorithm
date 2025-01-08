package Baekjoon;

import java.io.*;

public class Main_5717 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;

        while (!(input = br.readLine()).equals("0 0") ) {
            String[] friends = input.split(" ");
            System.out.println(Integer.parseInt(friends[0]) + Integer.parseInt(friends[1]));
        }
    }
}
