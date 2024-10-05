// 10994. 별 찍기 - 19
package Baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_10994 {
    public static void drawStars(int st, char[][] arr, int n) {
        // 종료 조건
        if (n <= 0) {
            return;
        }
        // 별 찍기
        for (int i = st; i < st + 4 * (n - 1) + 1; i++) {
            arr[st][i] = '*';  // 상단 행
            arr[i][st] = '*';  // 왼쪽 열
            arr[st + 4 * (n-1)][i] = '*';  // 하단 행
            arr[i][st + 4 * (n-1)] = '*';  // 오른쪽 열
        }
        drawStars(st+2, arr, n-1);  // 다음 재귀 호출
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int size = 4 * (N-1) + 1;
        char[][] stars = new char[size][size];

        // 빈 칸으로 초기화
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                stars[i][j] = ' ';
            }
        }

        drawStars(0, stars, N);  // 재귀함수 호출
        // 출력
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                System.out.print(stars[i][j]);
            }
            System.out.println();
        }
    }
}
