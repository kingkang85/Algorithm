package Baekjoon.HashSet;

import java.io.*;
import java.util.*;

/**
 * 25757. 임스와 함께하는 미니게임
 *
 * 1. 플레이어 중복되지 않도록 저장
 * 2. 게임 종류에 따라 나눈 몫 구하기
 */
public class Main_25757 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        String game = st.nextToken();

        Set<String> players = new HashSet<>();
        for (int i = 0; i < N; i++) {
            players.add(br.readLine());
        }

        int result = 0;
        switch (game) {
            case "Y" -> result = players.size();
            case "F" -> result = players.size() / 2;
            case "O" -> result = players.size() / 3;
        }

        System.out.println(result);
    }
}
