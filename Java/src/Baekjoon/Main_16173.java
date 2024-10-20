// 16173. 점프왕 쩰리
package Baekjoon;
import java.io.*;
import java.util.*;

public class Main_16173 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }

    }

    public static void bfs(int sti, int stj, int n) {
        Queue<Integer> q = new LinkedList<>();
        int[][] visited = new int[n][n];

        q.offer((sti, stj));
    }
}
