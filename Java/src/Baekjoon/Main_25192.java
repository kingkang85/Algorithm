package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_25192 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Set<String> chats = new HashSet<>();
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            String s = br.readLine();

            if (s.equals("ENTER")) {
                chats.clear();
            } else {
                if (chats.contains(s)) continue;
                chats.add(s);
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}
