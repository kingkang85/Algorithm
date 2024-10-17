// 1236. 성 지키기
package Baekjoon;
import java.io.*;
import java.util.*;

public class Main_1236 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 이차원 배열 입력 받기
        char[][] arr = new char[N][M];
        for (int i = 0; i < N; i++) {
            String row = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = row.charAt(j);
            }
        }

        // 가로 확인
        int cntR = 0;
        for (int i = 0; i < N; i++) {
            int cnt = 0;
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 'X') {
                    cnt++;
                }
            }
            // '.'으로만 이루어진 행 개수 세기
            if (cnt == 0) {
                cntR++;
            }
        }

        // 세로 확인
        int cntC = 0;
        for (int i = 0; i < M; i++) {
            int cnt = 0;
            for (int j = 0; j < N; j++) {
                if (arr[j][i] == 'X') {
                    cnt++;
                }
            }
            // '.'으로만 이루어진 열 개수 세기
            if (cnt == 0) {
                cntC++;
            }
        }
        // 둘 중 최댓값이 추가 경비원의 최솟값
        System.out.println(Math.max(cntR, cntC));
    }
}
