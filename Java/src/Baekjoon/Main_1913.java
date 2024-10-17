// 1913. 달팽이
package Baekjoon;
import java.io.*;

public class Main_1913 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int num = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][N];

        int r = 0, c = 0, d = 0, targetR = 0, targetC = 0;
        int val = N * N;
        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};
        while (val > 0) {
            arr[r][c] = val;

            if (val == num) {
                targetR = r + 1;
                targetC = c + 1;
            }
            int nr = r + dr[d];
            int nc = c + dc[d];

            // 배열의 범위가 넘어가거나 값이 이미 있으면 방향 전환
            if (nr < 0 || nr >= N || nc < 0 || nc >= N || arr[nr][nc] != 0) {
                d = (d+1) % 4;
                nr = r + dr[d];
                nc = c + dc[d];
            }
            r = nr;
            c = nc;
            val--;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(arr[i][j]).append(" ");
            }
            sb.append("\n");
        }
        sb.append(targetR).append(" ").append(targetC);
        System.out.println(sb);
    }
}