// 6609. 모기 곱셈
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_6609 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s;
        while ((s = br.readLine()) != null) {
            StringTokenizer st = new StringTokenizer(s);
            int M = Integer.parseInt(st.nextToken());
            int P = Integer.parseInt(st.nextToken());
            int L = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            int R = Integer.parseInt(st.nextToken());
            int S = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            for (int i = 0; i < N; i++) {
                int newM = P / S;
                int newP = L / R;
                int newL = M * E;

                M = newM;
                P = newP;
                L = newL;
            }
            System.out.println(M);
        }
    }
}