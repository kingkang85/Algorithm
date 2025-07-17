package Baekjoon.BinarySearch;

import java.io.*;
import java.util.*;

/**
 * 10815. 숫자 카드
 *
 * 1. 주어진 카드 오름차순 정렬
 * 2. 이분 탐색으로 카드 찾기
 */
public class Main_10815 {
    static int[] cards;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        cards = new int[N];
        for (int i = 0; i < N; i++) cards[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(cards);

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            if (findCard(Integer.parseInt(st.nextToken()))) {
                sb.append(1).append(' ');
            } else {
                sb.append(0).append(' ');
            }
        }

        System.out.println(sb);
    }

    /**
     * 이분 탐색으로 특정 숫자가 카드에 있는지 확인
     * @param number 찾고자 하는 숫자
     * @return 카드가 존재하면 true, 없으면 false
     */
    static boolean findCard(int number) {
        int left = 0;
        int right = cards.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (cards[mid] == number) {
                return true;
            } else if (cards[mid] < number) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }
}
