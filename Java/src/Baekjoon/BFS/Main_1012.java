package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_1012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            int[][] field = new int[N][M];

            for (int j = 0; j < K; j++) {
                st = new StringTokenizer(br.readLine());
                int c = Integer.parseInt(st.nextToken());
                int r = Integer.parseInt(st.nextToken());
                field[r][c] = 1;
            }

            boolean[][] visited = new boolean[N][M];

            int result = 0;
            for (int n = 0; n < N; n++) {
                for (int m = 0; m < M; m++) {
                    if (!visited[n][m] && field[n][m] == 1) {
                        bfs(visited, field, n, m);
                        result++;
                    }
                }
            }

            System.out.println(result);
        }
    }

    static void bfs(boolean[][] visited, int[][] field, int str, int stc) {
        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};

        int R = field.length;
        int C = field[0].length;

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{str, stc});
        visited[str][stc] = true;

        while (!q.isEmpty()) {
            int[] newPos = q.poll();
            int r = newPos[0];
            int c = newPos[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nr < R && nc >= 0 && nc < C && !visited[nr][nc] && field[nr][nc] == 1) {
                    q.offer(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            }
        }
    }
}
