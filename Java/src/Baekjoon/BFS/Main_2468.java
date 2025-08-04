package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_2468 {
    static int N;
    static int[][] area;
    static boolean[][] visited;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        area = new int[N][N];
        Set<Integer> heights = new HashSet<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int height = Integer.parseInt(st.nextToken());
                heights.add(height);
                area[i][j] = height;
            }
        }

        int maxCount = 1;
        for (int height : heights) {
            visited = new boolean[N][N];
            int count = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j] && area[i][j] > height) {
                        bfs(i, j, height);
                        count++;
                    }
                }
            }

            maxCount = Math.max(maxCount, count);
        }

        System.out.println(maxCount);
    }

    static void bfs(int str, int stc, int height) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{str, stc});
        visited[str][stc] = true;

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int r = now[0], c = now[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];

                if (nr >= 0 && nr < N && nc >= 0 && nc < N && !visited[nr][nc] && area[nr][nc] > height) {
                    q.offer(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            }
        }
    }
}
