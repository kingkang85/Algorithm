package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_2583 {
    static int M, N;
    static boolean[][] paper;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static ArrayList<Integer> areas;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        paper = new boolean[M][N];

        while (K-- > 0) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            for (int i = M - y2; i < M - y1; i++) {
                for (int j = x1; j < x2; j++) {
                    paper[i][j] = true;
                }
            }
        }

        int count = 0;
        areas = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (!paper[i][j]) {
                    bfs(i, j);
                    count++;
                }
            }
        }

        System.out.println(count);

        Collections.sort(areas);
        for (int area : areas) {
            sb.append(area).append(' ');
        }
        System.out.println(sb.toString().trim());
    }

    static void bfs(int str, int stc) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{str, stc});
        paper[str][stc] = true;
        int area = 1;

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int r = now[0], c = now[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];

                if (nr >= 0 && nr < M && nc >= 0 && nc < N && !paper[nr][nc]) {
                    q.offer(new int[]{nr, nc});
                    paper[nr][nc] = true;
                    area++;
                }
            }
        }

        areas.add(area);
    }
}
