package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_4963 {
    static int w, h;
    static int[][] map;
    static boolean[][] visited;
    static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dc = {0, 1, 1, 1, 0, -1, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            if (w == 0 && h == 0) {
                break;
            }

            map = new int[h][w];
            visited = new boolean[h][w];

            for (int i = 0; i < h; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < w; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int count = 0;
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (!visited[i][j] && map[i][j] == 1) {
                        bfs(i, j);
                        count++;
                    }
                }

            }

            sb.append(count).append('\n');
        }

        System.out.println(sb);
    }

    static void bfs(int str, int stc) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{str, stc});
        visited[str][stc] = true;

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int r = now[0], c = now[1];

            for (int i = 0; i < 8; i++) {
                int nr = r + dr[i], nc = c + dc[i];

                if (nr >= 0 && nr < h && nc >= 0 && nc < w && !visited[nr][nc] && map[nr][nc] == 1) {
                    q.offer(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            }
        }
    }
}
