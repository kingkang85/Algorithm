package Baekjoon.DFS;

import java.io.*;
import java.util.*;

public class Main_2668 {
    static int[] nums;
    static boolean[] visited;
    static boolean[] finished;
    static List<Integer> result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        nums = new int[N+1];

        for (int i = 1; i <= N; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }

        result = new ArrayList<>();
        visited = new boolean[N+1];
        finished = new boolean[N+1];

        for (int i = 1; i <= N; i++) {
           if (!visited[i]) {
               dfs(i);
           }
        }

        Collections.sort(result);
        System.out.println(result.size());
        for (int num : result) {
            System.out.println(num);
        }
    }

    static void dfs(int node) {
        visited[node] = true;
        int next = nums[node];

        if (!visited[next]) {
            dfs(next);
        } else if (!finished[next]) {
            int current = next;
            while (true) {
                result.add(current);
                if (current == node) break;
                current = nums[current];
            }
        }

        finished[node] = true;
    }
}
