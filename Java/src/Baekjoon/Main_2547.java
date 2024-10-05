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
            for (int j = 0; j < N; j++) {
                BigInteger candy = new BigInteger(br.readLine());
                candies = candies.add(candy);
            }
            // 총합이 학생 수로 나누어떨어지는지 확인
            BigInteger result = new BigInteger("0");
            result = candies.mod(BigInteger.valueOf(N));
            if (result.equals(BigInteger.ZERO)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
