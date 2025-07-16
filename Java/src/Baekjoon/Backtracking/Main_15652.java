package Baekjoon.Backtracking;

import java.io.*;
import java.util.*;

/**
 * 15652. N과 M (4)
 *
 *  재귀로 중복 조합 구하기
 *  1. 종료 조건은 고른 개수가 M개가 되었을 때
 *      - result 배열의 값을 출력하고 종료
 *  2. for문은 인자로 넘어온 인덱스부터 시작
 *      - 이전에 고른 값 이상만 선택 가능하여 중복 조합이 됨
 *  3. 재귀로 고른 개수와 현재 인덱스를 넘겨줌
 */
public class Main_15652 {
    static int N, M;
    static int[] result;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        result = new int[M];

        comb(0, 1);
        System.out.println(sb);
    }

    static void comb(int depth, int start) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(result[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i <= N; i++) {
            result[depth] = i;
            comb(depth + 1, i);
        }
    }
}
