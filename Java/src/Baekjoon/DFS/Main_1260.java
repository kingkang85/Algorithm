package Baekjoon.DFS;

import java.io.*;
import java.util.*;

public class Main_1260 {
    static int N, V;
    static ArrayList<Integer>[] graph;
    static boolean[] dfsVisited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 0; i <= N; i++) {
            Collections.sort(graph[i]);
        }

        dfsVisited = new boolean[N+1];
        dfs(V, dfsVisited);
        sb.append('\n');
        bfs();

        System.out.println(sb);
    }

    static void dfs(int node, boolean[] visited) {
        visited[node] = true;
        sb.append(node).append(' ');

        for (int next : graph[node]) {
            if (!dfsVisited[next]) {
                dfs(next, visited);
            }
        }
    }

    static void bfs() {
        Queue<Integer> q = new LinkedList<>();
        boolean[] bfsVisited = new boolean[N+1];

        q.offer(V);
        bfsVisited[V] = true;

        while (!q.isEmpty()) {
            int now = q.poll();
            sb.append(now).append(' ');

            for (int next : graph[now]) {
                if (!bfsVisited[next]) {
                    q.offer(next);
                    bfsVisited[next] = true;
                }
            }
        }
    }
}
