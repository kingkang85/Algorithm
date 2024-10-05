// 1977. 완전제곱수
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1977 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());

        int sum = 0;  // 완전제곱수의 합
        int min = Integer.MAX_VALUE;  // 최솟값
        for (int i = 0; i * i <= N ; i++) {
            int square = i * i;
            if (square >= M && square <= N) {
                sum += square;
                // 최솟값 비교
                if (min > square) {
                    min = square;
                }
            }
        }

        if (sum == 0) {
            System.out.println(-1);  // 완전제곱수가 없는 경우
        } else {
            System.out.println(sum);
            System.out.println(min);
        }
    }
}