// 1551. 수열의 변화
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1551 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nums = br.readLine().split(" ");
        int N = Integer.parseInt(nums[0]);
        int K = Integer.parseInt(nums[1]);

        String[] seq = br.readLine().split(",");
        int[] result = new int[N];
        for (int i = 0; i < N; i++) {
            result[i] = Integer.parseInt(seq[i]);
        }

        for (int i = 0; i < K; i++) {
            int[] tmp = new int[N - 1 - i];
            for (int j = 0; j < tmp.length; j++) {
                tmp[j] = result[j + 1] - result[j];
            }
            result = tmp;
        }

        for (int i = 0; i < result.length; i++) {
            if (i > 0) System.out.print(",");
            System.out.print(result[i]);
        }
    }
}
