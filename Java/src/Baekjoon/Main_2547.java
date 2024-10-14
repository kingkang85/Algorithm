// 2547. 사탕 선생 고창영
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main_2547 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            br.readLine();
            int N = Integer.parseInt(br.readLine());  // 학생 수
            BigInteger candies = BigInteger.ZERO;  // 캔디의 총합
            // 캔디 총합 구하기
            for (int j = 0; j < N; j++) {
                long candy = Long.parseLong(br.readLine());
                candies = candies.add(BigInteger.valueOf(candy));
            }
            // 총합이 학생 수로 나누어떨어지는지 확인
            int result = 0;
            result = candies.mod(BigInteger.valueOf(N)).intValue();

            if (result == 0) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}