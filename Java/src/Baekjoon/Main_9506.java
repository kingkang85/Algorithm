// 9506. 약수들의 합
package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_9506 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            int num = Integer.parseInt(br.readLine());
            if (num == -1) break;

            ArrayList<Integer> divisors = new ArrayList<>();
            int sum = 0;

            for (int i = 1; i < num; i++) {
                if (num % i == 0) {
                    divisors.add(i);
                    sum += i;
                }
            }

            if (sum == num) {
                sb.append(num).append(" = ").append(divisors.get(0));
                for (int i = 1; i < divisors.size(); i++) {
                    sb.append(" + ").append(divisors.get(i));
                }
            } else {
                sb.append(num).append(" is NOT perfect.");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}