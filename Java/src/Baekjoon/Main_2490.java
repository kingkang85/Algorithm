// 2490. 윷놀이
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_2490 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] arr = new int[3][4];
        for (int i = 0; i < 3; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < 4; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }

        for (int i = 0; i < 3; i++) {
            int cnt = 0;
            for (int j = 0; j < 4; j++) {
                if (arr[i][j] == 0) {
                    cnt++;
                }
            }
            switch (cnt) {
                case 1:
                    System.out.println("A");
                    break;
                case 2:
                    System.out.println("B");
                    break;
                case 3:
                    System.out.println("C");
                    break;
                case 4:
                    System.out.println("D");
                    break;
                default:
                    System.out.println("E");
            }
        }
    }
}
