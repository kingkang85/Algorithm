package Programmers.Impl;

import java.util.*;

// Lv1. 가장 가까운 같은 글자
public class SameLetters {
    public int[] sameLetters(String s) {
        int[] answer = new int[s.length()];
        Map<Character, Integer> lastSeen = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            answer[i] = i - lastSeen.getOrDefault(c, i+1);
            lastSeen.put(c, i);
        }

        return answer;
    }

    public static void main(String[] args) {
        SameLetters c = new SameLetters();
        System.out.println(c.sameLetters("banana"));
    }
}
