package Baekjoon.BFS;

import java.io.*;
import java.util.*;

public class Main_1325 {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[b].add(a);
        }

        int maxCount = 0;
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            int count = bfs(i);

            if (count > maxCount) {
                result.clear();
                result.add(i);
                maxCount = count;
            } else if (count == maxCount) {
                result.add(i);
            }
        }

        for (int num : result) {
            sb.append(num).append(' ');
        }

        System.out.println(sb.toString().trim());
    }

    static int bfs(int num) {
        visited = new boolean[N+1];
        Queue<Integer> q = new LinkedList<>();

        q.offer(num);
        visited[num] = true;
        int count = 1;

        while (!q.isEmpty()) {
            int now = q.poll();

            for (int next : graph[now]) {
                if (!visited[next]) {
                    q.offer(next);
                    visited[next] = true;
                    count++;
                }
            }
        }

        return count;
    }
}
