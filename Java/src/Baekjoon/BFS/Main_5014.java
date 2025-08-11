package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_5014 {
    static int F, S, G;
    static int[] direction = new int[2];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        F = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
        direction[0] = Integer.parseInt(st.nextToken());
        direction[1] = -Integer.parseInt(st.nextToken());

        int result = bfs();
        if (result == -1) {
            System.out.println("use the stairs");
        } else {
            System.out.println(result);
        }
    }

    static int bfs() {
        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[F+1];

        q.offer(new int[]{S, 0});
        visited[S] = true;

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int pos = now[0], count = now[1];

            if (pos == G) {
                return count;
            }

            for (int d : direction) {
                int next = pos + d;

                if (next >= 1 && next <= F && !visited[next]) {
                    q.offer(new int[]{next, count + 1});
                    visited[next] = true;
                }
            }
        }

        return -1;
    }
}
