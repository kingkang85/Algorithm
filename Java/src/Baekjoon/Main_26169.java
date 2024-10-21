package Baekjoon;
import java.io.*;
import java.util.*;

public class Main_26169 {
    static int n = 5;
    static int[][] arr = new int[n][n];
    static Stack<int[]> stack = new Stack<>();
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(input[j]);
            }
        }

        String[] nums = br.readLine().split(" ");
        int r = Integer.parseInt(nums[0]);
        int c = Integer.parseInt(nums[1]);

        br.close();
        System.out.println(dfs(r, c, 0, 0));

    }

    static int dfs(int r, int c, int moveCnt, int appleCnt) {
        if (moveCnt > 3) {
            return 0;
        }

        if (arr[r][c] == 1) {
            appleCnt++;
        }

        if (appleCnt >= 2) {
            return 1;
        }

        int tmp = arr[r][c];
        arr[r][c] = -1;

        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];

            if (nr >= 0 && nr < n && nc >= 0 && nc < n && arr[nr][nc] != -1) {
                if (dfs(nr, nc, moveCnt + 1, appleCnt) == 1) {
                    arr[r][c] = tmp;
                    return 1;
                }
            }
        }
        arr[r][c] = tmp;
        return 0;
    }
}