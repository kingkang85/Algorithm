package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_11507 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringBuilder sb = new StringBuilder();

        int[] cnt = new int[4];
        Set<String> cardSet = new HashSet<>();

        boolean found = false;
        for (int i = 0; i < input.length(); i += 3) {
            String card = input.substring(i, i+3);
            if (cardSet.contains(card)) {
                found = true;
            }
            cardSet.add(card);

            switch (card.charAt(0)) {
                case 'P': cnt[0]++; break;
                case 'K': cnt[1]++; break;
                case 'H': cnt[2]++; break;
                case 'T': cnt[3]++; break;
            }
        }

        for (int i = 0; i < 4; i++) {
            sb.append(13 - cnt[i]).append(' ');
        }

        if (found) System.out.println("GRESKA");
        else System.out.println(sb);
    }
}
