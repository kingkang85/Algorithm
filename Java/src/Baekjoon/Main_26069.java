package Baekjoon;

import java.io.*;
import java.util.*;

public class Main_26069 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        Set<String> people = new HashSet<>();
        people.add("ChongChong");

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            String person1 = st.nextToken();
            String person2 = st.nextToken();

            if (people.contains(person1)) {
                people.add(person2);
            } else if (people.contains(person2)) {
                people.add(person1);
            }
        }

        System.out.println(people.size());
    }
}
