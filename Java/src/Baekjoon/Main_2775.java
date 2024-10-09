// 2775. 부녀회장이 될테야
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_2775 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int k = Integer.parseInt(br.readLine());  // k층
            int n = Integer.parseInt(br.readLine());  // n호

            int[] apart = new int[n + 1];
            for (int j = 0; j < n + 1; j++) {
                apart[j] = j;
            }

            for (int j = 0; j < k; j++) {
                continue;
            }
        }

    }
}
