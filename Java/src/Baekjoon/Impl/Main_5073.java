package Baekjoon.Impl;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_5073 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true)  {
            st = new StringTokenizer(br.readLine());
            int side1 = Integer.parseInt(st.nextToken());
            int side2 = Integer.parseInt(st.nextToken());
            int side3 = Integer.parseInt(st.nextToken());

            if (side1 == 0 && side2 == 0 && side3 == 0) {
                break;
            }

            int[] sides = {side1, side2, side3};
            Arrays.sort(sides);

            if (sides[2] >= sides[0] + sides[1]) {
                System.out.println("Invalid");
                continue;
            }

            if (side1 == side2 && side2 == side3) {
                System.out.println("Equilateral");
            } else if (side1 == side2 || side2 == side3 || side1 == side3) {
                System.out.println("Isosceles");
            } else {
                System.out.println("Scalene");
            }
        }
    }
}
