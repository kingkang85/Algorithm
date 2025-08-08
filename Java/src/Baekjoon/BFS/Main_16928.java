package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_16928 {
    static int[] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        map = new int[101];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            map[Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            map[Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken());
        }

        System.out.println(playGame());
    }

    static int playGame() {
        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[101];

        q.offer(new int[]{1, 0});
        visited[1] = true;

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int pos = now[0], count = now[1];

            if (pos == 100) {
                return count;
            }

            for (int i = 1; i <= 6; i++) {
                int next = pos + i;

                if (next <= 100 && !visited[next]) {
                    if (map[next] != 0) {
                        next = map[next];
                    }
                    q.offer(new int[]{next, count + 1});
                    visited[next] = true;
                }
            }
        }

        return -1;
    }
}
