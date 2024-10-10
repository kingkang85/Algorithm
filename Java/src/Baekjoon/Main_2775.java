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
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());
            
            int[] apt = new int[n];

            // 0층 거주민 구하기
            for (int j = 0; j < n; j++) {
                apt[j] = j + 1;
            }

            // k층까지 한층씩 올라가며 거주민 구하기
            for (int j = 0; j < k; j++) {
                for (int l = 1; l < n; l++) {
                    apt[l] += apt[l - 1];
                }
            }
            System.out.println(apt[n-1]);
        }
    }
}
