package Baekjoon.Tree;

import java.io.*;
import java.util.*;

/**
 * 11725. 트리의 부모 찾기
 *
 * 1. 인접 리스트로 트리 표현
 * 2. BFS로 부모 찾기
 */
public class Main_11725 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        ArrayList<Integer>[] tree = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            tree[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            tree[a].add(b);
            tree[b].add(a);
        }

        int[] parent = new int[N+1];
        boolean[] visited = new boolean[N+1];
        Queue<Integer> q = new LinkedList<>();

        q.offer(1);
        visited[1] = true;

        while (!q.isEmpty()) {
            int current = q.poll();

            for (int next : tree[current]) {
                if (!visited[next]) {
                    parent[next] = current;
                    q.offer(next);
                    visited[next] = true;
                }
            }
        }

        for (int i = 2; i <= N; i++) {
            System.out.println(parent[i]);
        }
    }
}
