package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_6593 {
    static int L, R, C;
    static char[][][] building;
    static boolean[][][] visited;
    static int stl, str, stc;

    static int[] dl = {-1, 1, 0, 0, 0, 0};
    static int[] dr = {0, 0, -1, 0, 1, 0};
    static int[] dc = {0, 0, 0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            L = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());

            if (L == 0 && R == 0 && C == 0) {
                break;
            }

            building = new char[L][R][C];
            visited = new boolean[L][R][C];

            for (int i = 0; i < L; i++) {
                for (int j = 0; j < R; j++) {
                    String floor = br.readLine();
                    for (int k = 0; k < C; k++) {
                        Character c = floor.charAt(k);
                        if (c == 'S') {
                            stl = i; str = j; stc = k;
                        }
                        building[i][j][k] = c;
                    }
                }
                br.readLine();
            }

            int result = bfs();
            if (result == -1) {
                sb.append("Trapped!").append('\n');
            } else {
                sb.append("Escaped in ").append(result).append(" minute(s).").append('\n');
            }
        }

        System.out.println(sb);
    }

    static int bfs() {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{stl, str, stc, 0});
        visited[stl][str][stc] = true;

        while(!q.isEmpty()) {
            int[] pos = q.poll();
            int l = pos[0], r = pos[1], c = pos[2], minute = pos[3];

            if (building[l][r][c] == 'E') {
                return minute;
            }

            for (int i = 0; i < 6; i++) {
                int nl = l + dl[i], nr = r + dr[i], nc = c + dc[i];
                if (nl >= 0 && nl < L && nr >= 0 && nr < R && nc >= 0 && nc < C
                        && !visited[nl][nr][nc] && building[nl][nr][nc] != '#') {
                    q.offer(new int[]{nl, nr, nc, minute+1});
                    visited[nl][nr][nc] = true;
                }
            }
        }

        return -1;
    }
}
