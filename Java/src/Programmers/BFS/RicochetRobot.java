package Programmers.BFS;

import java.util.*;

public class RicochetRobot {
    int[] dx = {-1, 0, 1, 0};
    int[] dy = {0, 1, 0, -1};

    public int ricochetRobot(String[] board) {
        int rows = board.length;
        int cols = board[0].length();

        int startX = -1, startY = -1, goalX = -1, goalY = -1;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                char c = board[i].charAt(j);
                if (c == 'R') {
                    startX = i;
                    startY = j;
                } else if (c == 'G') {
                    goalX = i;
                    goalY = j;
                }
            }
        }

        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[rows][cols];

        q.offer(new int[]{startX, startY, 0});
        visited[startX][startY] = true;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            int moves = current[2];

            if (x == goalX && y == goalY) {
                return moves;
            }

            for (int d = 0; d < 4; d++) {
                int[] newPos = slide(board, x, y, d);
                int nx = newPos[0];
                int ny = newPos[1];

                if (visited[nx][ny] || (nx == x && ny == y)) {
                    continue;
                }

                visited[nx][ny] = true;
                q.offer(new int[]{nx, ny, moves+1});
            }
        }

        return -1;
    }

    private int[] slide(String[] board, int x, int y, int direction) {
        int rows = board.length;
        int cols = board[0].length();

        int nx = x;
        int ny = y;

        while (true) {
            int nextX = nx + dx[direction];
            int nextY = ny + dy[direction];

            if (nextX < 0 || nextX >= rows || nextY < 0 || nextY >= cols || board[nextX].charAt(nextY) == 'D') {
                break;
            }

            nx = nextX;
            ny = nextY;
        }

        return new int[]{nx, ny};
    }
}
