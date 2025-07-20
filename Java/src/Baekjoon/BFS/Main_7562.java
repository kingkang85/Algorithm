package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_7562 {
    static int[] dr = {-1, -2, -2, -1, 1, 2, 2, 1};
    static int[] dc = {-2, -1, 1, 2, 2, 1, -1, -2};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int l = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine());
            int startR = Integer.parseInt(st.nextToken());
            int startC = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int endR = Integer.parseInt(st.nextToken());
            int endC = Integer.parseInt(st.nextToken());

            System.out.println(bfs(l, startR, startC, endR, endC));
        }
    }

    static int bfs(int l, int startR, int startC, int endR, int endC) {
        boolean[][] visited = new boolean[l][l];
        Queue<int[]> q = new LinkedList<>();

        q.offer(new int[]{startR, startC, 0});
        visited[startR][startC] = true;

        while (!q.isEmpty()) {
            int[] pos = q.poll();
            int r = pos[0], c = pos[1], move = pos[2];

            if (r == endR && c == endC) {
                return move;
            }

            for (int i = 0; i < 8; i++) {
                int nr = r + dr[i], nc = c + dc[i];

                if (nr >= 0 && nr < l && nc >= 0 && nc < l && !visited[nr][nc]) {
                    q.offer(new int[]{nr, nc, move + 1});
                    visited[nr][nc] = true;
                }
            }
        }

        return -1;
    }
}
