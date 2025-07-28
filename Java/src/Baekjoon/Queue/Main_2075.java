package Baekjoon.Queue;

import java.io.*;
import java.util.*;

/**
 * 2075. N번째 큰 수
 *
 * 1. 최소 힙에 수 저장
 * 2. 힙의 사이즈가 N개를 넘어가면 작은 수부터 삭제
 * 3. 최종적으로 N개 중 가장 앞의 원소가 N번째로 큰 수
 */
public class Main_2075 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                pq.offer(Integer.parseInt(st.nextToken()));

                if (pq.size() > N) {
                    pq.poll();
                }
            }
        }

        System.out.println(pq.peek());
    }
}
