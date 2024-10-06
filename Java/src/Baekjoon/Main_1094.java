// 1094. 막대기
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1094 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        int stickCnt = 0;

        // X를 2로 나누어가면서 1인 비트의 개수를 셈
        while (X > 0) {
            if (X % 2 == 1) {
                stickCnt++;
            }
            X /= 2;
        }
        System.out.println(stickCnt);
    }
}