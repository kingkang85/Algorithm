package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_1926 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] paper = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        boolean[][] visited = new boolean[n][m];
        int count = 0, maxValue = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && paper[i][j] == 1) {
                    maxValue = Math.max(maxValue, bfs(visited, paper, i, j));
                    count++;
                }
            }
        }

        System.out.println(count);
        System.out.println(maxValue);
    }

    static int bfs(boolean[][] visited, int[][] paper, int str, int stc) {
        int area = 1;

        int R = paper.length;
        int C = paper[0].length;

        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{str, stc});
        visited[str][stc] = true;

        while (!q.isEmpty()) {
            int[] newPos = q.poll();
            int r = newPos[0];
            int c = newPos[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];

                if (nr >= 0 && nr < R && nc >= 0 && nc < C && !visited[nr][nc] && paper[nr][nc] == 1) {
                    q.offer(new int[]{nr, nc});
                    visited[nr][nc] = true;
                    area++;
                }
            }
        }

        return area;
    }
}
