// 16173. 점프왕 쩰리
package Baekjoon;
import java.io.*;
import java.util.*;

public class Main_16173 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }
        System.out.println(bfs(0, 0, n, arr));
    }

    static String bfs(int sti, int stj, int n, int[][] arr) {
        Queue<int[]> q = new LinkedList<>();
        int[][] visited = new int[n][n];

        q.offer(new int[] {sti, stj});
        visited[sti][stj] = 1;

        int[] di = {0, 1};
        int[] dj = {1, 0};

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int i = now[0];
            int j = now[1];

            if (i == n-1 && j == n-1) {
                return "HaruHaru";
            }

            for (int k = 0; k < 2; k++) {
                int ni = i + di[k] * arr[i][j];
                int nj = j + dj[k] * arr[i][j];

                if (ni >= 0 && ni < n && nj >= 0 && nj < n && visited[ni][nj] == 0 && arr[ni][nj] != 0) {
                    q.offer(new int[] {ni, nj});
                    visited[ni][nj] = 1;
                }
            }
        }
        return "Hing";
    }
}
